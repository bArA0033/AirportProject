from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_upload_to(instance, filename):
    return f'profile_pics/{instance.username}/{filename}'

class User(AbstractUser):
    # data
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(blank=True)
    profile_pic = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)

    # dates
    date_of_birth = models.DateField(blank=True, null=True)


class Employee(models.Model):
    # inner classes
    class Positions(models.TextChoices):
        manager = 'ma', 'manager'
        administrator = 'ad', 'administrator'
        gate_gard = 'gg', 'gate_gard'
        flight_crew = 'fc', 'flight_crew'
        pilot = 'pi', 'pilot'
        airport_employee = 'ae', 'airport_employee'
        passenger = 'pa', 'passenger'

    # foreign relations
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='employee_profile')

    # data
    job_position = models.CharField(choices=Positions.choices, default=Positions.passenger, max_length=100)

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
        active = 'ac', 'active'
        under_repair = 'ur', 'under_repair'
        retired = 're', 'retired'
    # foreign relations
    company = models.ForeignKey(AirCompany, on_delete=models.CASCADE, related_name='airplanes')
    # data
    status = models.CharField(choices=Status.choices, default=Status.active)
    capacity = models.PositiveIntegerField(default=0)
