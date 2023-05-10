from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Restuarant



def registerpage(request):
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
        return redirect('login')
    else:
     return render(request, "StaffReg/registerpage.html")
def Login(request):
    if request.method=='POST':
       name = request.POST.get('uname')
       password = request.POST.get('pass')
       user = authenticate(request, username=name, password=password)
       if user is not None:
            login(request, user)
            return redirect(reverse('staff-home'))
            
       else:
            return HttpResponse('Error, user does not exist')
    else:       
     return render(request, 'StaffReg/login.html')
    
def logoutuser(request):
    logout(request)
    return redirect(reverse('login'))
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'StaffReg/profile.html', context)



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('staff-home')
    else:
        form = UserRegisterForm()
    return render(request, 'StaffReg/register.html', {'form': form})
def restuarant(request):
    context= {
        'restuarants' : Restuarant.objects.all()
    }
   
    return render(request, "staffReg/restuarants.html", context)
