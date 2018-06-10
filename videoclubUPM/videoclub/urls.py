from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.signIn, name='login'),
    path('process_login', views.process_login, name='process_login'),
    path('process_logout', views.process_logout, name='process_logout'),
    path('film', views.film, name='film'),
    path('search_film', views.search_film, name='search_film'),
    path('signup', views.signUp, name='signup'),
    path('process_signup', views.process_signup, name='process_signup')
]