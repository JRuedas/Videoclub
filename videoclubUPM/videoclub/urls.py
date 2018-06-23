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
    path('editProfile', views.edit_profile, name='edit_profile'),
    path('changePassword', views.change_password, name='change_password'),
    path('films', views.films, name='films'),
    path('film', views.film, name='film'),
    path('newFilm', views.add_film, name='add_film'),
    path('forbidden', views.forbidden, name='forbidden'),
    path('redirectForbidden', views.redirect_forbidden, name='redirect_forbidden'),
    path('add_film/search', views.find_filmsAdd, name='find_filmsAdd')
]