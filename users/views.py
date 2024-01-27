from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import *
from .forms import *

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect('home')  
        messages.error(request, "Invalid Credentials")
        return render(request, 'users/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logged out successfully")
            return redirect('login') 
        else:
            messages.error(request, "You aren't logged in")
            return redirect('login')
    
class SignupView(View):
    def get(self, request):
        form = SingupForm()
        return render(request, 'users/signup.html', {'form': form})
    
    def post(self, request):
        form = SingupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home') 
        return render(request, 'users/signup.html', {'form': form})
