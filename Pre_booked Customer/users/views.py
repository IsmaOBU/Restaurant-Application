from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Booking

def Bookings(request):
    context = {
        'bookings': Booking.objects.all()
    }
    return render(request, 'users/booking.html', context)

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        phone = request.POST.get('phone')
        address = request.POST.get('add')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.phone_no = phone
        new_user.address = address

        new_user.save()
        return redirect('users-booking')
    else:
     return render(request, "users/register.html")
def Login(request):
    if request.method=='POST':
       name = request.POST.get('uname')
       password = request.POST.get('pass')
       user = authenticate(request, username=name, password=password)
       if user is not None:
            login(request, user)
            return redirect(reverse('users-home'))
            
       else:
            return HttpResponse('Error, user does not exist')
    else:       
     return render(request, 'users/login.html')
    
def logoutuser(request):
    logout(request)
    return redirect(reverse('login'))


   




