from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from . import forms
# Create your views here.

def index(request):
    context = {}
    return render(request, "videoclub/index.html", context)

def signIn(request):
    context = {}
    return render(request, "videoclub/login.html", context)

def doLogin (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authenticated
            login(request, user)
            return redirect("/videoclub/films")
        else:
            messages.error(request,'Incorrect user or password')
            return redirect("/videoclub/login")

def doLogout (request):
    logout(request)
    return redirect("/videoclub/")

def list_users(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "videoclub/list_users.html", context)

def create_user(request):
    form = forms.CreateUserForm(request.POST)

    if request.method == 'POST':

        form = forms.CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            return redirect("/videoclub/users")
    else:
        form = forms.CreateUserForm()

    return render(request, "videoclub/create_user.html", {'form': form})

def modify_user(request):

    username = request.GET.get('username')
    user = User.objects.get_by_natural_key(username)

    if request.method == 'POST':

        form = forms.UserUpdate(request.POST, instance=user)

        if form.is_valid():
            user = form.save()
            user.save()
            
            return redirect("/videoclub/users")
    else:
        form = forms.UserUpdate(instance=user)
        context = {
            'form': form,
            "user" : user
            }
        return render(request, "videoclub/modify_user.html", context)

def delete_user(request):

    username = request.GET.get('username')
    user = User.objects.get_by_natural_key(username)
    user.delete()
    return redirect("/videoclub/users")

def films(request):
    context = {}
    return render(request, "videoclub/films.html", context)

def film(request):
    context = {}
    return render(request, "videoclub/film.html", context)

def add_film(request):
    context = {}
    return render(request, "videoclub/add_film.html", context)