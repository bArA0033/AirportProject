from django import forms

from airport.models import Flight


class FlightForm(forms.ModelForm):
    model = Flight
    fields = '__all__'