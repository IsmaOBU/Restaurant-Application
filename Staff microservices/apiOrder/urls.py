from django.urls import path
from . import views

urlpatterns = [
    path('apiOrder/', views.getData),
     path('add/', views.addOrder),
]
