from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", max_length=254, help_text="Required")
    # Profile
    birth_date = forms.DateField(label="Date of Birth", help_text="Required. Format: YYYY-MM-DD")
    phone_number = forms.CharField(label="Phone Number", max_length=10)
    delivery_address = forms.CharField(label="Delivery Address", max_length=100)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", )
