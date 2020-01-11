from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.

def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

def create_movie(request):
    return render(request, 'movie-create.html')

def logout(request):
    """ log the user out """
    auth.logout(request)
    messages.success(request, "You have succesfully been logged out")
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""
    return render(request, 'login.html')
