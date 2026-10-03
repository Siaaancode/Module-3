from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Links bookings to user accounts
class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )