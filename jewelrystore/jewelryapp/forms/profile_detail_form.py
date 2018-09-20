from django.forms import ModelForm
from jewelryapp.models import Profile

class ProfileDetailModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["birth_date", "phone_number", "delivery_address"]
