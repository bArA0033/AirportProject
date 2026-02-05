from django.contrib import admin

from airport.models import *


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    model = Flight
    list_display = ['id','take_off_time','origin','destination','status']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['user', 'job_position', 'date_of_employment']


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    model = Airplane
    list_display = ['company', 'status', 'capacity']

@admin.register(AirCompany)
class AirCompanyAdmin(admin.ModelAdmin):
    model = AirCompany
    list_display = ['name', 'city', 'phone', 'email']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
