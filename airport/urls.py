from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import *
from . import views
app_name = 'airport'

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('flight_detail/<pk>',views.flight_detail,name='flight_detail'),
    path('create_flight/',views.create_flight,name='create_flight'),
    path('update_flight/<pk>',views.update_flight,name='update_flight'),
    path('delete_flight/<pk>',views.delete_flight,name='delete_flight'),
]