from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

from airport.forms import FlightForm
from airport.models import Flight, Employee


def home(request):
    flights = Flight.objects.all()
    logged = request.user.is_authenticated
    if logged:
        person = request.user
    else:
        person = None
    context = {
        'flights': flights,
        'person': person,
        'logged': logged,
    }
    return render(request, 'partials/home.html', context)


@login_required
def profile(request):
    flights = Flight.objects.all()
    if request.user.employee:
        if request.user.employee.job_position == Employee.Positions.Manager:
            flights = Flight.objects.all()
        elif request.user.employee.job_position == Employee.Positions.Pilot:
            flights = Flight.objects.filter(pilot=request.user.employee)
        person = request.user.employee
        passenger = False
    else:
        flights = Flight.objects.filter(passengers=request.user.passenger)
        person = request.user.passenger
        passenger = True

    context = {
        'flights': flights,
        'person': person,
        'passenger': passenger,
    }

    return render(request, 'partials/profile.html', context)


def log_out(request):
    logout(request)
    return redirect('airport:home')


def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    manager = None
    if request.user.employee:
        person = request.user.employee
        if person.job_position == Employee.Positions.Manager:
            manager = True
    else:
        person = request.user.passenger

    context = {
        'flight': flight,
        'person': person,
        'manager': manager,
    }
    return render(request, 'partials/flight_detail.html', context)


def create_flight(request):
    flight = None
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save()
            return redirect('airport:flight_detail', flight.pk)
    form = FlightForm()
    context = {
        'form': form,
        'flight': flight,
    }
    return render(request, 'partials/creat_flight.html', context)


def update_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('airport:flight_detail', flight.pk)
    form = FlightForm(instance=flight)
    context = {
        'flight': flight,
        'form': form
    }
    return render(request, 'partials/creat_flight.html', context)

def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    flight.delete()
    return redirect('airport:home')