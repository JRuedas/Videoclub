from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {}
    return render(request, "videoclub/index.html", context)

def login(request):
    context = {}
    return render(request, "videoclub/login.html", context)

texts = []

def process_login (request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        texts.append(username)
        texts.append(password)
        context['texts'] = texts
    return render(request, "videoclub/search_film.html", context)