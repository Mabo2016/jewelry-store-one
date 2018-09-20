from django.forms import ModelForm
from registration.models import Profile

class ProfileDetailModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["birth_date", "phone_number", "delivery_address"]
