from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Links bookings to user accounts
class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Table(models.Model):
    # Identifies each table
    table_number = models.PositiveIntegerField(unique=True)
    #How many people it can accommodate
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} ({self.seats} seats)"

table = models.ForeignKey(
    Table,
    on_delete=models.PROTECT,
    related_name='bookings'
)