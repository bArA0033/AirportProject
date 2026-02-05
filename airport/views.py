from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from airport.models import Flight


def home(request):
    flights = Flight.objects.all()
    return render(request,'home.html',{'flights':flights})

@login_required
def profile(request):
    if request.user.employee:
        flights = Flight.objects.filter(pilot=request.user.employee)
        person = request.user.employee
        passenger = False
    else:
        flights = Flight.objects.filter(passengers=request.user.passenger)
        person = request.user.passenger
        passenger = True

    context = {
        'flights':flights,
        'person':person,
        'passenger':passenger,
    }

    return render(request,'profile.html',context)

