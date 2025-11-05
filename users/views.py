from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.urls import reverse


def landing(request):
    return render(request, 'users/index.html')

def dashboard(request):
    return render(request, "users/dashboard.html")

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('dashboard'))
    else: 
        form = CustomUserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})