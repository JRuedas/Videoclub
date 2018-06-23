from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

@login_required(login_url='/videoclub/login')
def doLogout (request):
    logout(request)
    return redirect("/videoclub/")

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def list_users(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, "videoclub/list_users.html", context)

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def create_user(request):
    form = forms.CreateUserForm(request.POST)

    if request.method == 'POST':

        form = forms.CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/videoclub/users")
    else:
        form = forms.CreateUserForm()

    return render(request, "videoclub/create_user.html", {'form': form})

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def modify_user(request):
    username = request.GET.get('username')
    user = User.objects.get_by_natural_key(username)

    if request.method == 'POST':

        form = forms.UserUpdateForm(request.POST, instance=user)

        if form.is_valid():
            form.save()            
            return redirect("/videoclub/users")
    else:
        form = forms.UserUpdateForm(instance=user)
        context = {
            'form': form,
            "user" : user
            }
        return render(request, "videoclub/modify_user.html", context)

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def delete_user(request):

    username = request.GET.get('username')
    user = User.objects.get_by_natural_key(username)
    user.delete()
    return redirect("/videoclub/users")

@login_required(login_url='/videoclub/login')
def edit_profile(request):
    user = request.user

    if request.method == 'POST':

        form = forms.EditProfileForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/videoclub/films")
    else:
        form = forms.EditProfileForm(instance=user)
        context = {
            'form': form,
            "user" : user
            }
        return render(request, "videoclub/edit_profile.html", context)

@login_required(login_url='/videoclub/login')
def change_password(request):
    user = request.user

    if request.method == 'POST':

        form = PasswordChangeForm(data=request.POST, user=user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)            
            return redirect("/videoclub/films")
        else:
            return redirect('/videoclub/changePassword ')
    else:
        form = PasswordChangeForm(user=user)
        context = {
            'form': form,
            "user" : user
            }
        return render(request, "videoclub/change_password.html", context)

@login_required(login_url='/videoclub/login')
def films(request):
    context = {}
    return render(request, "videoclub/films.html", context)

@login_required(login_url='/videoclub/login')
def film(request):
    context = {}
    return render(request, "videoclub/film.html", context)

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def add_film(request):
    context = {}
    return render(request, "videoclub/add_film.html", context)

def forbidden(request):
    context = {}
    return render(request, "videoclub/forbidden.html", context)

def redirect_forbidden(request):
    if request.user.is_authenticated:
        return redirect("/videoclub/films")
    else:
        return redirect("/videoclub/login")
