from django.forms import ModelForm
from jewelryapp.models import User

class UserDetailModelForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
