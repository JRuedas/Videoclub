from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    context = {}
    return render(request, "videoclub/index.html", context)

def signIn(request):
    context = {}
    return render(request, "videoclub/login.html", context)

def film(request):
    context = {}
    return render(request, "videoclub/film.html", context)

def search_film(request):
    context = {}
    return render(request, "videoclub/search_film.html", context)

def process_login (request):
    context = {}

    #Default option, not authenticated, return to index TODO: show error
    response = render(request, "videoclub/index.html", context)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authenticated
            login(request, user)
            response = render(request, "videoclub/search_film.html", context)
            
    return response