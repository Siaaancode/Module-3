from datetime import timedelta, time

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Booking, Table
from .views import table_is_available, BOOKING_DURATION


class BookingViewTests(TestCase):
    """Test the Kokoro restaurant booking system."""

    def setUp(self):
        """Create users and a table for each test."""
        self.customer = User.objects.create_user(
            username="customer1",
            password="TestPassword123!"
        )
        self.other_customer = User.objects.create_user(
            username="customer2",
            password="TestPassword123!"
        )

        self.table = Table.objects.create(
            table_number=1,
            seats=4,
            is_active=True
        )

        self.booking_date = timezone.localdate() + timedelta(days=1)
        self.booking_time = time(12, 0)

    def create_test_booking(self, **kwargs):
        """Create a booking for testing."""
        details = {
            "user": self.customer,
            "table": self.table,
            "booking_date": self.booking_date,
            "booking_time": self.booking_time,
            "guests": 2,
            "duration_minutes": BOOKING_DURATION,
            "status": "confirmed",
        }
        details.update(kwargs)
        return Booking.objects.create(**details)

    def test_booking_page_requires_login(self):
        """Check that customers must log in to book."""
        response = self.client.get(reverse("booking_page"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_profile_requires_login(self):
        """Check that customers must log in to view their profile."""
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_valid_booking_is_saved(self):
        """Check that a valid booking saves the correct details."""
        self.client.force_login(self.customer)

        response = self.client.post(
            reverse("booking_page"),
            {
                "booking_date": self.booking_date.isoformat(),
                "booking_time": "12:00",
                "guests": 3,
            },
        )

        self.assertRedirects(response, reverse("profile"))

        booking = Booking.objects.get(user=self.customer)

        self.assertEqual(booking.table, self.table)
        self.assertEqual(booking.booking_date, self.booking_date)
        self.assertEqual(booking.booking_time, self.booking_time)
        self.assertEqual(booking.guests, 3)
        self.assertEqual(booking.status, "confirmed")

    def test_overlapping_confirmed_booking_blocks_table(self):
        """Check that overlapping bookings cannot use the same table."""
        self.create_test_booking()

        available = table_is_available(
            self.table,
            self.booking_date,
            time(13, 0),
        )

        self.assertFalse(available)

    def test_cancelling_booking_makes_table_available(self):
        """Check that cancellation releases a table."""
        booking = self.create_test_booking()
        self.client.force_login(self.customer)

        response = self.client.post(
            reverse("cancel_booking", args=[booking.pk])
        )

        self.assertRedirects(response, reverse("profile"))

        booking.refresh_from_db()
        self.assertEqual(booking.status, "cancelled")

        available = table_is_available(
            self.table,
            self.booking_date,
            self.booking_time,
        )

        self.assertTrue(available)

    def test_customer_cannot_edit_another_customers_booking(self):
        """Check that customers cannot edit other people's bookings."""
        booking = self.create_test_booking()
        self.client.force_login(self.other_customer)

        response = self.client.get(
            reverse("edit_booking", args=[booking.pk])
        )

        self.assertEqual(response.status_code, 404)

    def test_customer_cannot_cancel_another_customers_booking(self):
        """Check that customers cannot cancel other people's bookings."""
        booking = self.create_test_booking()
        self.client.force_login(self.other_customer)

        response = self.client.post(
            reverse("cancel_booking", args=[booking.pk])
        )

        self.assertEqual(response.status_code, 404)

        booking.refresh_from_db()
        self.assertEqual(booking.status, "confirmed")

    def test_booking_with_past_date_is_rejected(self):
        """Check that bookings cannot be made for past dates."""
        self.client.force_login(self.customer)

        response = self.client.post(
            reverse("booking_page"),
            {
                "booking_date": (
                    timezone.localdate() - timedelta(days=1)
                ).isoformat(),
                "booking_time": "12:00",
                "guests": 2,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "today or a future date")
        self.assertEqual(Booking.objects.count(), 0)

    def test_booking_outside_opening_hours_is_rejected(self):
        """Check that bookings cannot start before opening."""
        self.client.force_login(self.customer)

        response = self.client.post(
            reverse("booking_page"),
            {
                "booking_date": self.booking_date.isoformat(),
                "booking_time": "11:00",
                "guests": 2,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 0)

    def test_party_larger_than_available_tables_is_rejected(self):
        """Check that an oversized party cannot book a table."""
        self.client.force_login(self.customer)

        response = self.client.post(
            reverse("booking_page"),
            {
                "booking_date": self.booking_date.isoformat(),
                "booking_time": "12:00",
                "guests": 5,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no longer available")
        self.assertEqual(Booking.objects.count(), 0)