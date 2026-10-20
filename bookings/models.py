"""Define the database models for restaurant tables and customer bookings."""

from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    """Represent a physical table available at the restaurant."""

    # Assign a unique number to identify each restaurant table.
    table_number = models.PositiveIntegerField(unique=True)

    # Store the maximum number of guests the table can accommodate.
    seats = models.PositiveIntegerField()

    # Allow staff to make a table unavailable without deleting it.
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return a readable description of the table."""
        return f"Table {self.table_number} ({self.seats} seats)"


class Booking(models.Model):
    """Store a customer's reservation and its allocated table."""

    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    # Link the booking to the customer's user account.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Links the booking to an allocated restaurant table.    
    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        related_name='bookings',
        null=True,
        blank=True
    )

    # Store the date and time of the reservation.
    booking_date = models.DateField(
        null=True,
        blank=True
    )

    booking_time = models.TimeField(
        null=True,
        blank=True
    )

    # Record the number of guests included in the booking.
    guests = models.PositiveIntegerField(
        default=2
    )

    # Store the expected booking duration in minutes.
    duration_minutes = models.PositiveIntegerField(
        default=120
    )

    # Track the current status of the reservation.
    status = models.CharField(
     max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed'
    )

    def __str__(self):
        """Return a readable summary of the booking."""
        return (
            f"Booking {self.pk} - "
            f"{self.booking_date} {self.booking_time} - "
            f"{self.table}"
        )