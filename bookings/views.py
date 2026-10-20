"""Import utilities required to handle restaurant booking views."""

from datetime import datetime, date, time, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import SignUpForm
from .models import Booking, Table

# Define the booking rules used throughout the application.
# Set the duration of each restaurant booking to 120 minutes (2 hours).
BOOKING_DURATION = 120


# Allow booking start times at 30-minute intervals.
SLOT_INTERVAL = 30


# Set the restaurant's daily opening time to 12:00 (midday).
OPENING_TIME = time(12, 0)


# Set the restaurant's daily closing time to 22:00 (10:00 pm).
CLOSING_TIME = time(22, 0)


def index(request):
    """Render the homepage."""
    return render(request, 'index.html')


def menu(request):
    """Render the menu page."""
    return render(request, "menu.html")


def booking_page(request):
    """Render the booking page."""
    return render(request, "booking_page.html")


def signup(request):
    """Handle customer registration by validating and saving the signup form.

    Display an empty form for GET requests. For valid POST requests,
    create the user's account, display a success message and redirect
    the customer to the login page. If the form is invalid, redisplay
    it with validation errors.
    """
    # Check whether the customer has submitted the signup form.
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # Save the account only if all form fields are valid.
        if form.is_valid():
            form.save()

            # Display a confirmation message and redirect to login.
            messages.success(
                request,
                'Your account has been created successfully.'
            )
            return redirect('login')
    else:
        # Display an empty signup form for a new visitor.
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    """Display the logged-in customer's profile and restaurant bookings.

    Retrieve the customer's bookings, ordered by booking date and time,
    and provide them to the profile template along with the current
    local date. Require authentication to access this page.
    """
    # Retrieve only bookings belonging to the currently logged-in customer.
    # Sort bookings by date first, then by time.
    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('booking_date', 'booking_time')

    # Prepare the data to be passed to the profile template.
    context = {
        'bookings': bookings,
        'today': timezone.localdate(),
    }

    # Render the profile page and display the customer's booking details.
    return render(request, 'profile.html', context)


@login_required
def create_booking(request):
    """Validate and create a restaurant booking for the logged-in customer.

    Validate the submitted date, time and party size, ensuring the booking
    falls within the restaurant's opening hours and is in the future.
    Find a suitable available table, save the confirmed booking to the
    database and redirect the customer to their profile. If validation
    fails or no table is available, redisplay the booking page with an
    appropriate error message.
    """
    # Process the booking when the form is submitted.
    if request.method == "POST":
        try:
            # Convert submitted values into Python date, time
            # and integer objects for validation and database storage.
            booking_date = date.fromisoformat(
                request.POST.get("booking_date", "")
            )
            booking_time = time.fromisoformat(
                request.POST.get("booking_time", "")
            )
            guests = int(request.POST.get("guests", ""))

            # Reject bookings with fewer than one guest.
            if guests < 1:
                raise ValueError

        except (TypeError, ValueError):
            # Redisplay the form if any submitted value is missing
            # or cannot be converted into the required data type.
            return render(request, "booking_page.html", {
                "error": "Please select a valid date, "
                "time and number of guests.",
            })

        # Prevent customers from booking dates in the past.
        if booking_date < timezone.localdate():
            return render(request, "booking_page.html", {
                "error": "Please choose today or a future date.",
            })

        # Calculate the booking's start and end times using the
        # restaurant's configured booking duration.
        start = datetime.combine(booking_date, booking_time)
        end = start + timedelta(minutes=BOOKING_DURATION)

        # Combine the selected date with the restaurant's opening
        # and closing times to establish the permitted booking window.
        opening = datetime.combine(booking_date, OPENING_TIME)
        closing = datetime.combine(booking_date, CLOSING_TIME)

        # Ensure the selected time follows the required slot interval
        # and the entire booking fits within opening hours.
        if (
            booking_time.minute % SLOT_INTERVAL != 0
            or booking_time.second != 0
            or booking_time.microsecond != 0
            or start < opening
            or end > closing
        ):
            return render(request, "booking_page.html", {
                "error": "Please select one of the available booking times.",
            })

        # Prevent customers from selecting a time that has already
        # passed when making a booking for the current day.
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

        # Group the table availability check and booking creation
        # into a database transaction.
        with transaction.atomic():
            # Retrieve active tables that can accommodate the party.
            # Lock the selected table records during the transaction
            # and check smaller suitable tables first.
            suitable_tables = list(
                Table.objects.select_for_update().filter(
                    is_active=True,
                    seats__gte=guests,
                ).order_by("seats", "table_number")
            )

            # Initialise the table variable before searching.
            table = None

            # Find the first suitable table without an overlapping
            # confirmed booking at the requested date and time.
            for candidate in suitable_tables:
                if table_is_available(
                    candidate,
                    booking_date,
                    booking_time
                ):
                    table = candidate
                    break

            # Stop the booking process if no suitable table is available.
            if table is None:
                return render(request, "booking_page.html", {
                    "error": "Sorry, that time is no longer available. "
                    "Please choose another time.",
                })

            # Create the confirmed booking with the customer, allocated
            # table, selected date and time, and party size.
            Booking.objects.create(
                user=request.user,
                table=table,
                booking_date=booking_date,
                booking_time=booking_time,
                guests=guests,
                duration_minutes=BOOKING_DURATION,
                status="confirmed",
            )
            # Redirect the customer to their profile after booking.
            return redirect("profile")

    # Display an empty booking page when the customer first visits it.
    return render(request, "booking_page.html")


def table_is_available(
    table,
    booking_date,
    booking_time,
    exclude_booking=None
):
    """Check whether a table is free for the requested time."""
    # Calculate the requested booking's start and end times.
    requested_start = datetime.combine(
        booking_date,
        booking_time,
    )
    requested_end = requested_start + timedelta(
        minutes=BOOKING_DURATION
    )

    # Retrieve confirmed bookings for this table on the requested date.
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

    # Compare the requested time with each existing booking.
    for booking in existing_bookings:
        # Ignore older or incomplete bookings without a time.
        if booking.booking_time is None:
            continue

        # Calculate when the existing booking starts and finishes.
        existing_start = datetime.combine(
            booking.booking_date,
            booking.booking_time,
        )
        existing_end = existing_start + timedelta(
            minutes=booking.duration_minutes
        )

        # Two bookings overlap if each starts before the other one ends.
        if (
            requested_start < existing_end
            and existing_start < requested_end
        ):
            return False

    # No overlapping confirmed booking was found.
    return True


def find_available_table(booking_date, booking_time, guests):
    """Find a suitable table or return None."""
    # Only consider active tables that can seat the whole party.
    tables = Table.objects.filter(
        is_active=True,
        seats__gte=guests,
    ).order_by("seats", "table_number")

    # Return the first table that is free for the requested time.
    for table in tables:
        if table_is_available(table, booking_date, booking_time):
            return table

    # No suitable table is available for this date and time.
    return None


def available_times(request):
    """Return available booking times as JSON for the booking form."""
    # Read the selected date and party size from the frontend request.
    date_value = request.GET.get("date")
    guests_value = request.GET.get("guests", "2")

    try:
        # Convert the submitted values and validate the party size.
        booking_date = date.fromisoformat(date_value)
        guests = int(guests_value)

        if guests < 1:
            raise ValueError

    except (TypeError, ValueError):
        # Return an HTTP 400 response if the request contains invalid data.
        return JsonResponse(
            {"error": "Please choose a valid date and guest count."},
            status=400,
        )

    # Return no times for dates in the past.
    if booking_date < timezone.localdate():
        return JsonResponse({"times": []})

    # Prepare the time range and interval used to generate booking slots.
    times = []
    current = datetime.combine(booking_date, OPENING_TIME)
    closing = datetime.combine(booking_date, CLOSING_TIME)
    duration = timedelta(minutes=BOOKING_DURATION)
    interval = timedelta(minutes=SLOT_INTERVAL)

    # Check every possible start time that allows the full booking duration.
    while current + duration <= closing:
        slot_time = current.time()

        # On today's date, exclude times that have already passed.
        is_future_time = (
            booking_date != timezone.localdate()
            or current > datetime.combine(
                booking_date,
                timezone.localtime().time().replace(tzinfo=None),
            )
        )

        if is_future_time:
            # Only offer a slot if a suitable table is available.
            table = find_available_table(
                booking_date,
                slot_time,
                guests,
            )
            if table is not None:
                # Add the value for the form and label for the interface.
                times.append({
                    "value": slot_time.strftime("%H:%M"),
                    "label": slot_time.strftime("%H:%M"),
                })

        # Advance to the next booking slot, even if this one is unavailable.
        current += interval

    # Send the complete list back to the frontend as JSON.
    return JsonResponse({"times": times})


# Offers user the ability to edit their bookings.
@login_required
def edit_booking(request, booking_id):
    """Allow the customer to edit their confirmed booking."""
    booking = get_object_or_404(
        Booking,
        pk=booking_id,
        user=request.user,
    )

    # Only confirmed bookings can be edited.
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
                "error": "Please enter a valid date, time and "
                "number of guests.",
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
            or booking_time.second != 0
            or booking_time.microsecond != 0
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


# Offers users the ability to cancel their bookings.
@login_required
def cancel_booking(request, booking_id):
    """Allow the customer to cancel their confirmed booking."""
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
