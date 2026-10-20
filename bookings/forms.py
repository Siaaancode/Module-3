
"""Define the customer registration form."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Collect customer details and validate new account credentials."""

    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="First name",
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Last name",
    )
    email = forms.EmailField(
        required=True,
        label="Email address",
    )

    class Meta:
        """Configure the user model anbd fields displayed on the form."""
        
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )