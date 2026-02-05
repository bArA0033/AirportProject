from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

from airport.models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['airplane', 'pilot', 'origin', 'destination', 'status', 'take_off_time', 'land_time']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

