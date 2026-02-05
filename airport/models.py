from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_upload_to(instance, filename):
    return f'profile_pics/{instance.username}/{filename}'

class User(AbstractUser):
    # data
    phone_number = models.CharField(max_length=11)
    profile_pic = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)

    # dates
    date_of_birth = models.DateField(blank=True, null=True)


class Employee(models.Model):
    # inner classes
    class Positions(models.TextChoices):
        Manager = 'ma', 'manager'
        Administrator = 'ad', 'administrator'
        Gate_gard = 'gg', 'gate_gard'
        Flight_crew = 'fc', 'flight_crew'
        Pilot = 'pi', 'pilot'
        Airport_employee = 'ae', 'airport_employee'

    # foreign relations
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='employee')

    # data
    job_position = models.CharField(choices=Positions.choices, default=Positions.Airport_employee, max_length=100)

    # date
    date_of_employment = models.DateField()



class AirCompany(models.Model):
    # data
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Airplane(models.Model):
    # inner classes
    class Status(models.TextChoices):
        Active = 'ac', 'active'
        Under_repair = 'ur', 'under_repair'
        Retired = 're', 'retired'

    # foreign relations
    company = models.ForeignKey(AirCompany, on_delete=models.CASCADE, related_name='airplanes')

    # data
    status = models.CharField(choices=Status.choices, default=Status.Active)
    capacity = models.PositiveIntegerField(default=0)

class Flight(models.Model):
    # inner classes
    class Status(models.TextChoices):
        Waiting = 'wa', 'waiting'
        GateOpen = 'go', 'gate_open'
        Boarding = 'bo', 'boarding'
        LastCall = 'cl', 'last_call'
        GateClose = 'gc', 'gate_closed'
        TookOff = 'to', 'took_off'
        Landed = 'la', 'landed'

    # foreign relations
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')
    pilot = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='flights')
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    # data
    status = models.CharField(choices=Status.choices, default=Status.Waiting)
    take_off_time = models.TimeField()
    land_time = models.DateTimeField()

class Passenger(models.Model):
    # foreign relations
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='passenger')
    flights = models.ManyToManyField(Flight,related_name='passengers',blank=True)
