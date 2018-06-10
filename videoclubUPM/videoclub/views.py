from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

def index(request):
    context = {}
    return render(request, "videoclub/index.html", context)

def signIn(request):
    context = {}
    return render(request, "videoclub/login.html", context)

def signUp(request):
    context = {}
    return render(request, "videoclub/signup.html", context)

def film(request):
    context = {}
    return render(request, "videoclub/film.html", context)

def search_film(request):
    context = {}
    return render(request, "videoclub/search_film.html", context)

def process_login (request):
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authenticated
            login(request, user)
            return render(request, "videoclub/search_film.html", context)
        else:
            messages.error(request,'Incorrect user or password')
            return HttpResponseRedirect("/videoclub/login")

def process_logout (request):
    context = {}
    logout(request)
    return render(request, "videoclub/index.html", context)

def process_signup (request):
    context = {}

    if request.method == 'POST':
        form = UserCreationForm()
            
    return render(request, 'signup.html', {'form': form})