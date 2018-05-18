from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('process_login', views.process_login, name='process_login'),
    path('film', views.film, name='film'),
    path('search_film', views.search_film, name='search_film'),
]