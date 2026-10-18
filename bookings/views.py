from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from datetime import datetime, date, time, timedelta
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Booking, Table

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, "menu.html")

def booking_page(request):
    return render(request, "booking_page.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your account has been created successfully.'
            )
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def create_booking(request):
    # Booking form and booking logic
    if request.method == "POST":
        guests = request.POST.get("guests")
        booking_time = request.POST.get("booking_time")

        print("Number of guests:", guests)
        print("Booking time:", booking_time)

    return render(request, "booking_page.html")

BOOKING_DURATION = 120
SLOT_INTERVAL = 30
OPENING_TIME = time(12, 0)
CLOSING_TIME = time(22, 0)

def table_is_available(table, booking_date, booking_time):
    """Return True if the table has no bookings that overlap with the requested time slot."""

    requested_start = datetime.combine(booking_date, booking_time)
    requested_end = requested_start + timedelta(
        minutes=BOOKING_DURATION
    )
    existing_bookings = Booking.objects.filter(
        table=table,
        booking_date=booking_date,
        status="confirmed",
    )
    for booking in existing_bookings:
        if booking.booking_time is None:
            continue

        existing_start = datetime.Combine(
            booking.booking_date,
            booking.booking_time,
        )
        existing_end = existing_start + timedelta(
            minutes=booking.duration_minutes
        )
        if (
            requested_start < existing_end
            and existing_start < requested_end
        ):
            return False
    return True

def find_available_table(booking_date, booking_time, guests):
    """Find a suitable table or return None"""

    tables = Table.objects.filter(
        is_active=True,
        seats__gte=guests,
    ).order_by("seats",  "table_number")

    for table in tables:
        if table_is_available(table, booking_date, booking_time):
            return table

    return None

def available_times(request):
    date_value = request.GET.get("date")
    guests_value = request.GET.get("guests", "2")

    try:
        booking_date = date.fromisoformat(date_value)
        guests = int(guests_value)

        if guests < 1:
            raise ValueError

    except (TypeError, ValueError):
        return JsonResponse(
            {"error": "Please choose a valid date and guest count."},
            status=400,
        )

    if booking_date < timezone.localdate():
        return JsonResponse({"times": []})

    times = []
    current = datetime.combine(booking_date, OPENING_TIME)
    closing = datetime.combine(booking_date, CLOSING_TIME)
    duration = timedelta(minutes=BOOKING_DURATION)
    interval = timedelta(minutes=SLOT_INTERVAL)

    while current + duration <= closing:
        slot_time = current.time()

        if (
            booking_date != timezone.localdate()
            or current > datetime.combine(
                booking_date, timezone.localtime().time()
            )
        ):
            table = find_available_table(
                booking_date,
                slot_time,
                guests,
            )
            if table is not None:
                times.append({
                    "value": slot_time.strftime("%H:%M"),
                    "label": slot_time.strftime("%H:%M"),
                })

            current += interval

        return JsonResponse({"times": times})
