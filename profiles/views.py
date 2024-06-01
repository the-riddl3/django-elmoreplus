from django.http import HttpResponse
from django.shortcuts import render
from profiles.forms import LoginForm, ProfileForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Profile updated!")
        else:
            return HttpResponse("Invalid profile")
    else:
        form = ProfileForm(request.user)
    
    return render(request, 'profile.html', {"form": form})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User registered!")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {"form": form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
            else:
                return HttpResponse("Invalid login")
            return HttpResponse("User logged in!")
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {"form": form})
