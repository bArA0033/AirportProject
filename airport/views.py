from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

from airport.models import Flight


def home(request):
    flights = Flight.objects.all()
    logged = request.user.is_authenticated
    if logged:
        person = request.user
    else:
        person = None
    context = {
        'flights':flights,
        'person':person,
        'logged':logged,
    }
    return render(request, 'partials/home.html', context)

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

    return render(request, 'partials/profile.html', context)

def log_out(request):
    logout(request)
    return redirect('airport:home')

def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    context = {
        'flight':flight,
    }
    return render(request,'partials/flight_detail.html',context)