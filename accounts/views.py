from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.

def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

def create_movie(request):
    return render(request, 'movie-create.html')

def logout(request):
    """ log the user out """
    auth.logout(request)
    return redirect(reverse('index'))
