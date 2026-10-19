from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Stores the restaurant's physical tables.
class Table(models.Model):
    # Identifies each table
    table_number = models.PositiveIntegerField(unique=True)
    #How many people it can accommodate
    seats = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.seats} seats)"

# Links bookings to user accounts
class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
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

    booking_date = models.DateField(
        null=True,
        blank=True
    )

    booking_time = models.TimeField(
        null=True,
        blank=True
    )

    guests = models.PositiveIntegerField(
        default=2
    )

    duration_minutes = models.PositiveIntegerField(
        default=120
    )

    status = models.CharField(
     max_length=20,
        choices=STATUS_CHOICES,
        default='confirmed'
    )

    def __str__(self):
        return f"Booking {self.id} - {self.booking_date} {self.table}"