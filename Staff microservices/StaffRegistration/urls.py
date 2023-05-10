from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='staff-home'),

    path("registerpage", views.registerpage, name='registerpage'),
   
    path("login", views.Login, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("restuarants", views.restuarant, name='restuarant'),
]
 
