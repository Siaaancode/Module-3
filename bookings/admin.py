"""Configure the Django admin interface for restaurant tables and bookings."""

from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Customise the admin interface for managing restaurant tables."""

    list_display = ("table_number", "seats", "is_active")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Customise the admin interface for managing customer bookings."""
    
    list_display = (
        "id",
        "user",
        "booking_date",
        "booking_time",
        "guests",
        "table",
        "status",
        "special_requests",
    )

    list_filter = ("booking_date", "status")

    fields = (
        "user",
        "table",
        "booking_date",
        "booking_time",
        "guests",
        "duration_minutes",
        "status",
        "special_requests",
    )