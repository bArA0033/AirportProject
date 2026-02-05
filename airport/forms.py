from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User

from airport.models import Flight


class FlightForm(forms.ModelForm):
    model = Flight
    fields = '__all__'

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

