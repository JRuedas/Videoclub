from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.signIn, name='login'),
    path('films', views.process_login, name='process_login'),
    path('', views.process_logout, name='process_logout'),
    path('film', views.film, name='film'),
    path('search_film', views.search_film, name='search_film'),
    path('create_user', views.create_user, name='create_user'),
    path('list_users', views.list_users, name='list_users'),
    path('add_film', views.add_film, name='add_film')
]