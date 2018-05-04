from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {}
    return render(request, "videoclub/index.html", context)