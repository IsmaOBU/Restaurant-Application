from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.Bookings, name='users-booking'),

    path("register", views.register, name='register'),
   
    path("login", views.Login, name='login'),
    path("logout", views.logoutuser, name='logout'),
]
 
