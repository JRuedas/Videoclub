from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.signIn, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='doLogout'),
    path('users', views.list_users, name='list_users'),
    path('newUser', views.create_user, name='create_user'),
    path('changeUser', views.modify_user, name='modify_user'),
    path('deleteUser', views.delete_user, name='delete_user'),
    path('films', views.films, name='films'),
    path('film', views.film, name='film'),
    path('newFilm', views.add_film, name='add_film')
]