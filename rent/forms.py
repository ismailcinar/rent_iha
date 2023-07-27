# forms.py
from django import forms
from .models import UAV
from .models import RentalRecord
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_admin']

class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category', 'rental_price', 'image']
  # Add other fields if needed




class RentalRecordForm(forms.ModelForm):
    class Meta:
        model = RentalRecord
        fields = ['uav', 'start_date', 'end_date', 'renting_member']
        