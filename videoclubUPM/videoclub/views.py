from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from . import forms
import requests
# Create your views here.

key = "f6093d8fefcd7f83e17a8af193b48d8d"

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

def add_film(request):
    context = {}
    return render(request, "videoclub/add_film.html", context)

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

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if(form.is_valid):
            form.save()

    else:
        form = forms.SignUpForm()
            
    return render(request, 'videoclub/signup.html', {'form' : form})

# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
def find_filmsAdd(request):
    context={}
    
    if request.method == 'GET':
        searched = True
        text = request.GET['text_search']
        endpoint = 'https://api.themoviedb.org/3/search/movie?api_key={key_id}&query={text_id}'
        url = endpoint.format(key_id=key, text_id=text)
        response = requests.get(url)
        if response.status_code == 200: #SUCCESS
            search_result = response.json()
            results = search_result['results']

            for element in results:
                element['poster_path'] = 'http://image.tmdb.org/t/p/w185//%s' % element['poster_path']

            context = {
                'searched': searched,
                'results': results,
            }

    return render(request, 'videoclub/add_film.html', context)