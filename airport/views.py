from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from airport.models import Flight


def home(request):
    pass

@login_required
def profile(request):
    if request.user.employee:
        flights = Flight.objects.filter(pilot=request.user.employee)
        person = request.user.employee
    else:
        flights = Flight.objects.filter(passengers=request.user.passenger)
        person = request.user.passenger

    context = {
        'flights':flights,
        'person':person,
    }

    return render(request,'',context)