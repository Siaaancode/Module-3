from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib import messages
from datetime import datetime, date, time, timedelta
from django.db import transaction
from django.http import JsonResponse
from django.utils import timezone
from .models import Booking, Table
from django.contrib.auth.decorators import login_required

# Display the restaurant homepage
def index(request):
    return render(request, 'index.html')

# Display the restaurant menu
def menu(request):
    return render(request, "menu.html")

# Display the booking form and calendar
def booking_page(request):
    return render(request, "booking_page.html")

# Validate and create a new customer account
def signup(request):
    # Check whether the customer has submitted the signup form
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # Save the account only if all form fields are valid
        if form.is_valid():
            form.save()

            # Display a confirmation message and redirect to login
            messages.success(
                request,
                'Your account has been created successfully.'
            )
            return redirect('login')
    else:
        # Display an empty signup form for a new visitor
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# Creates a profile for users to view bookings
@login_required
def profile(request):
    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('booking_date', 'booking_time')

    context = {
        'bookings': bookings,
        'today': timezone.localdate(),
    }

    return render(request, 'profile.html', context)

# Validate the booking details and allocate an available table
@login_required
def create_booking(request):

    # Process the booking when the form is submitted
    if request.method == "POST":
        try:
            # Convert submitted values into Python date, time and integer types
            booking_date = date.fromisoformat(
                request.POST.get("booking_date", "")
            )
            booking_time = time.fromisoformat(
                request.POST.get("booking_time", "")
            )
            guests = int(request.POST.get("guests", ""))

            # Reject bookings with an invalid party size
            if guests < 1:
                raise ValueError

        except (TypeError, ValueError):
            # Return an error if any submitted value is invalid
            return render(request, "booking_page.html", {
                "error": "Please select a valid date, time and number of guests.",
            })
        
        # Prevent customers from booking dates in the past
        if booking_date < timezone.localdate():
            return render(request, "booking_page.html", {
                "error": "Please choose today or a future date.",
            })

        # Calculate the booking's start and end times
        start = datetime.combine(booking_date, booking_time)
        end = start + timedelta(minutes=BOOKING_DURATION)

        # Define the restaurant's opening and closing times for this date
        opening = datetime.combine(booking_date, OPENING_TIME)
        closing = datetime.combine(booking_date, CLOSING_TIME)

        # Ensure the booking starts at a permitted interval and fits
        # entirely within the restaurant's opening hours
        if (
            booking_time.minute % SLOT_INTERVAL != 0
            or start < opening
            or end > closing
        ):
            return render(request, "booking_page.html", {
                "error": "Please select one of the available booking times.",
            })

        # Reject booking times that have already passed today
        if (
            booking_date == timezone.localdate()
            and start <= datetime.combine(
                booking_date,
                timezone.localtime().time().replace(tzinfo=None),
            )
        ):
            return render(request, "booking_page.html", {
                "error": "Please choose a future booking time.",
            })

        # Group database operations into a transaction while checking
        # and assigning a table
        with transaction.atomic():
            # Find active tables with enough seats for the party
            # Check smaller suitable tables first to use capacity efficiently
            suitable_tables = list(
                Table.objects.select_for_update().filter(
                    is_active=True,
                    seats__gte=guests,
                ).order_by("seats", "table_number")
            )

            table = None

            # Find the first table without an overlapping confirmed booking
            for candidate in suitable_tables:
                if table_is_available(
                    candidate, booking_date, booking_time):
                    table = candidate
                    break

            # Stop if every suitable table is already booked
            if table is None:
                return render(request, "booking_page.html", {
                    "error": "Sorry, that time is no longer available. "
                        "Please choose another time.",
                })

            # Save the booking with its customer, allocated table and details
            Booking.objects.create(
                user=request.user,
                table=table,
                booking_date=booking_date,
                booking_time=booking_time,
                guests=guests,
                duration_minutes=BOOKING_DURATION,
                status="confirmed",
            )

            return redirect("profile")

    # Display the booking page when it is opened without a form submission
    return render(request, "booking_page.html")

# Booking rules used by the booking form and availability checker
BOOKING_DURATION = 120 # Each booking lasts 2 hours
SLOT_INTERVAL = 30 # Booking start times are 30 minutes apart
OPENING_TIME = time(12, 0)
CLOSING_TIME = time(22, 0)

def table_is_available(
        table,
        booking_date,
        booking_time,
        exclude_booking=None
):
    """Check whether a table is free for the requested time"""

    # Calculate the requested booking's start and end times
    requested_start = datetime.combine(
        booking_date,
        booking_time,
    )
    requested_end = requested_start + timedelta(
        minutes=BOOKING_DURATION
    )

    # Retrieve confirmed bookings for this table on the requested date
    existing_bookings = Booking.objects.filter(
        table=table,
        booking_date=booking_date,
        status="confirmed",
    )

    # Ignore the booking being edited, if applicable.
    if exclude_booking is not None:
        existing_bookings = existing_bookings.exclude(
            pk=exclude_booking.pk
        )

    # Compare the requested time with each existing booking
    for booking in existing_bookings:
        # Ignore older or incomplete bookings without a time
        if booking.booking_time is None:
            continue

        # Calculate when the existing booking starts and finishes
        existing_start = datetime.combine(
            booking.booking_date,
            booking.booking_time,
        )
        existing_end = existing_start + timedelta(
            minutes=booking.duration_minutes
        )

        # Two bookings overlap if each starts before the other one ends
        if (
            requested_start < existing_end
            and existing_start < requested_end
        ):
            return False

    # No overlapping confirmed booking was found
    return True

def find_available_table(booking_date, booking_time, guests):
    """Find a suitable table or return None"""

    # Only consider active tables that can seat the whole party
    tables = Table.objects.filter(
        is_active=True,
        seats__gte=guests,
    ).order_by("seats",  "table_number")

    # Return the first table that is free for the requested time
    for table in tables:
        if table_is_available(table, booking_date, booking_time):
            return table

    # No suitable table is available for this date and time
    return None

def available_times(request):
    """ Return available booking times as JSON for the booking form. """

    # Read the selected date and party size from the frontend request
    date_value = request.GET.get("date")
    guests_value = request.GET.get("guests", "2")

    try:
        # Convert the submitted values and validate the party size
        booking_date = date.fromisoformat(date_value)
        guests = int(guests_value)

        if guests < 1:
            raise ValueError

    except (TypeError, ValueError):
        # Return an HTTP 400 response if the request contains invalid data
        return JsonResponse(
            {"error": "Please choose a valid date and guest count."},
            status=400,
        )

    # Return no times for dates in the past
    if booking_date < timezone.localdate():
        return JsonResponse({"times": []})

    # Prepare the time range and interval used to generate booking slots
    times = []
    current = datetime.combine(booking_date, OPENING_TIME)
    closing = datetime.combine(booking_date, CLOSING_TIME)
    duration = timedelta(minutes=BOOKING_DURATION)
    interval = timedelta(minutes=SLOT_INTERVAL)

    # Check every possible start time that allows the full booking duration
    while current + duration <= closing:
        slot_time = current.time()

        # On today's date, exclude times that have already passed
        is_future_time = (
            booking_date != timezone.localdate()
            or current > datetime.combine(
                booking_date, timezone.localtime().time()
            )
        )

        if is_future_time:
            # Only offer a slot if a suitable table is available
            table = find_available_table(
                booking_date,
                slot_time,
                guests,
            )
            if table is not None:
                # Add the value for the form and label for the interface
                times.append({
                    "value": slot_time.strftime("%H:%M"),
                    "label": slot_time.strftime("%H:%M"),
                })

        # Advance to the next booking slot, even if this one is unavailable
        current += interval

    # Send the complete list back to the frontend as JSON.
    return JsonResponse({"times": times})

# Offers user the ability to edit their bookings
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        pk=booking_id,
        user=request.user,
    )

    # Only confirmed bookings can be edited
    if booking.status != "confirmed":
        return render(request, "profile.html", {
            "bookings": Booking.objects.filter(
                user=request.user
            ).order_by("booking_date", "booking_time"),
            "today": timezone.localdate(),
            "error": "Only confirmed bookings can be edited."
        })

    if request.method == "POST":
        try:
            booking_date = date.fromisoformat(
                request.POST.get("booking_date", "")
            )
            booking_time = time.fromisoformat(
                request.POST.get("booking_time", "")
            )
            guests = int(request.POST.get("guests", ""))

            if guests < 1:
                raise ValueError

        except (TypeError, ValueError):
            return render(request, "edit_booking.html", {
                "booking": booking,
                "today": timezone.localdate(),
                "error": "Please choose a date.",
            })
        if booking_date < timezone.localdate():
            return render(request, "edit_booking.html", {
                "booking": booking,
                "today": timezone.localdate(),
                "error": "Please choose today or a future date.",
            })

        start = datetime.combine(booking_date, booking_time)
        end = start + timedelta(minutes=BOOKING_DURATION)
        opening = datetime.combine(booking_date, OPENING_TIME)
        closing = datetime.combine(booking_date, CLOSING_TIME)

        if (
            booking_time.minute % SLOT_INTERVAL != 0
            or start < opening
            or end > closing
        ):
            return render(request, "edit_booking.html", {
                "booking": booking,
                "today": timezone.localdate(),
                "error": "Please choose a valid available booking time.",
            })

        if (
            booking_date == timezone.localdate()
            and start <= timezone.localtime().replace(
                tzinfo=None
            )
        ):
            return render(request, "edit_booking.html", {
                "booking": booking,
                "today": timezone.localdate(),
                "error": "Please choose a future booking time.",
            })

        with transaction.atomic():
            suitable_tables = list(
                Table.objects.select_for_update().filter(
                    is_active=True,
                    seats__gte=guests,
                ).order_by("seats", "table_number")
            )

            available_table = None

            for candidate in suitable_tables:
                if table_is_available(
                    candidate,
                    booking_date,
                    booking_time,
                    exclude_booking=booking,
                ):
                    available_table = candidate
                    break

            if available_table is None:
                return render(request, "edit_booking.html", {
                    "booking": booking,
                    "today": timezone.localdate(),
                    "error": (
                        "Sorry, no suitable tables are available "
                        "for that date and time."
                    ),
                })

            booking.booking_date = booking_date
            booking.booking_time = booking_time
            booking.guests = guests
            booking.table = available_table
            booking.duration_minutes = BOOKING_DURATION
            booking.save()

        return redirect("profile")

    return render(request, "edit_booking.html", {
        "booking": booking,
        "today": timezone.localdate(),
    })

# Offers users the ability to cancel their bookings
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        pk=booking_id,
        user=request.user,
    )

    if booking.status != "confirmed":
        return redirect("profile")

    if request.method == "POST":
        booking.status = "cancelled"
        booking.save(update_fields=["status"])
        return redirect("profile")

    return render(request, "cancel_booking.html", {
        "booking": booking,
    })