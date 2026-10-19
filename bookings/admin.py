from django.contrib import admin
from .models import Table, Booking

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number", "seats", "is_active")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "booking_date",
        "booking_time",
        "guests",
        "table",
        "status",
    )

    list_filter = ("booking_date", "status")