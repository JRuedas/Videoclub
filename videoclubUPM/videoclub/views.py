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
import requests
from videoclub.models import Movie, Cast
import ast
# Create your views here.

key = "f6093d8fefcd7f83e17a8af193b48d8d"

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
            return redirect("/videoclub/")

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
        form = forms.EditPasswordForm(data=request.POST, user=user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)            
            return redirect("/videoclub/films")
        else:
            messages.error(request,'Incorrect password')
            return redirect('/videoclub/changePassword')
    else:
        form = forms.EditPasswordForm(user=user)
        context = {
            'form': form,
            "user" : user
            }
        return render(request, "videoclub/change_password.html", context)

@login_required(login_url='/videoclub/login')
def films(request):
    context = {}

    films = Movie.objects.all()
    more_than_zero = False
    for movie in films:
        more_than_zero = True
        movie.url_poster = 'http://image.tmdb.org/t/p/w185/%s' % movie.url_poster
    
    context = {
        'more_than_zero': more_than_zero,
        'films': films
    } 

    return render(request, "videoclub/films.html", context)

@login_required(login_url='/videoclub/login')
def doSeeMore(request):
    context = {}
    if request.method == 'GET':
        id_movie = request.GET.get('id')
        found = True
        exist = True

        if not Movie.objects.filter(id_movie=id_movie).exists():
            return redirect('/videoclub/films')

        film = Movie.objects.get(id_movie=id_movie)
        url_poster = 'http://image.tmdb.org/t/p/w500/%s' % film.url_poster   

        cast_list = Cast.objects.prefetch_related('movies').filter(movies=film)
        
        context = {
            'found': found,
            'exist': exist,
            'film': film,
            'filmId': id_movie,
            'url_poster': url_poster,
            'cast_list': cast_list
        }
        return render(request, 'videoclub/film.html', context)
    else:
        return redirect('/videoclub/films')

@login_required(login_url='/videoclub/login')
def doFindFilms(request):
    context = {}
    
    if request.method == 'GET':
        text = request.GET['text_search']
        films = list(Movie.objects.raw('SELECT * FROM videoclub_movie WHERE title LIKE \'%'+text+'%\''))
        more_than_zero = True
        
        for movie in films:
            movie.url_poster = 'http://image.tmdb.org/t/p/w185/%s' % movie.url_poster 

        context = {
            'more_than_zero': more_than_zero,
            'films': films
        } 
        
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

# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
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
                element['poster_path'] = 'http://image.tmdb.org/t/p/w185/%s' % element['poster_path']
                
        context = {
                'searched': searched,
                'results': results,
            }        

    return render(request, 'videoclub/add_film.html', context)

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def doSeeMoreToAdd(request):
    context = {}
    
    id_movie = request.GET.get('id')
    endpoint_film = 'https://api.themoviedb.org/3/movie/{id_number}?api_key={key_id}'
    url_film = endpoint_film.format(key_id=key, id_number=id_movie)
    response_film = requests.get(url_film)
    if response_film.status_code == 200: #SUCCESS
        exist = False
        found = True
        result_film = response_film.json()
        poster_path_aux = result_film['poster_path']
        result_film['poster_path'] = 'http://image.tmdb.org/t/p/w500/%s' % result_film['poster_path']
        youtube_video = 'https://www.youtube.com/embed/KolfEhV-KiA?rel=0' 

        endpoint_video = 'https://api.themoviedb.org/3/movie/{id_number}/videos?api_key={key_id}'
        url_video = endpoint_video.format(key_id=key, id_number=id_movie)
        response_video = requests.get(url_video)
        if response_video.status_code == 200: #SUCCESS
            search_video = response_video.json()
            results = search_video['results']
            if results:
                first_video = results[0]
                youtube_video =  'https://www.youtube.com/embed/%s?rel=0' % first_video['key'] 

        endpoint_credits = 'https://api.themoviedb.org/3/movie/{id_number}/credits?api_key={key_id}'
        url_credits = endpoint_credits.format(key_id=key, id_number=id_movie)
        response_credits = requests.get(url_credits)
        if response_credits.status_code == 200: #SUCCESS
            search_credits = response_credits.json()
            cast_result = search_credits['cast']
            crew = search_credits['crew']
            cast_list=[]
            director = ''
            if len(cast_result) > 5:
                for i in range(5):
                    if cast_result[i]:
                        cast_aux = cast_result[i]
                        cast_list.append(cast_aux['name'])
            else:
                for member in cast_result:
                    cast_aux = member
                    cast_list.append(cast_aux['name'])
         
            for member in crew:
                if member['job'] == 'Director':
                    director = member['name']
                    break

        film = Movie()
        film.id_movie = result_film['id']
        film.title = result_film['title']
        film.original_title = result_film['original_title']
        film.overview = result_film['overview']
        film.date = result_film['release_date']
        film.director = director
        film.url_poster = poster_path_aux
        film.vote_average = result_film['vote_average']
        film.url_video = youtube_video
        film.budget = result_film['budget']
        film.revenue = result_film['revenue']
        film.original_language = result_film['original_language']
        film.status = result_film['status']
        film.runtime = result_film['runtime']
        url_poster = result_film['poster_path']

        movies = Movie.objects.filter(id_movie=id_movie)

        if movies:
            exist = True
        
        context = {
            'found': found,
            'exist': exist,
            'film': film,
            'filmId': id_movie,
            'url_poster': url_poster,
            'cast_list': cast_list,
        }
  
        return render(request, 'videoclub/film.html', context)
    else:
        return redirect('/videoclub/films')

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def doAddFilm(request):
    if request.method == 'POST':
        film = Movie()

        film.id_movie = request.POST['filmId']

        if not Movie.objects.filter(id_movie=film.id_movie).exists():
            film.title = request.POST['title']
            film.original_title = request.POST['original_title']
            film.overview = request.POST['overview']
            film.date = request.POST['release_date']
            film.director = request.POST['director']
            film.url_poster = request.POST['poster_url']
            film.vote_average = request.POST['vote_average']
            film.url_video = request.POST['video_url']
            film.budget = request.POST['budget']
            film.revenue = request.POST['revenue']
            film.original_language = request.POST['original_language']
            film.status = request.POST['status']
            film.runtime = request.POST['runtime']
        
            film.save()

            cast_list = request.POST['cast_list']
            cast_aux = ast.literal_eval(cast_list)
            for member in cast_aux:
                if Cast.objects.filter(name=member).exists():
                    Cast.objects.get(name=member).movies.add(film)
                else:
                    cast_member = Cast.objects.create(name=member)
                    cast_member.movies.add(film)
                    cast_member.save()

        return redirect("/videoclub/film?id="+film.id_movie)

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def doDelete(request):
    id_movie = request.GET.get('filmId')
    if Movie.objects.filter(id_movie=id_movie).exists():
        Movie.objects.get(id_movie=id_movie).delete()
    return redirect("/videoclub/film/add?id="+id_movie)

@login_required(login_url='/videoclub/login')
@staff_member_required(login_url='/videoclub/forbidden')
def edit_film(request):
    context = {}
    filmId = request.GET.get('filmId')
    film = Movie.objects.get(id_movie=filmId)

    if request.method == 'POST':
        form = forms.EditFilmForm(request.POST, instance=film)

        if form.is_valid():
            form.save()
            return redirect("/videoclub/films")
    else:
        form = forms.EditFilmForm(instance=film)
        context = {
            'form': form,
            "film" : film
            }
        return render(request, "videoclub/edit_film.html", context)

def forbidden(request):
    context = {}
    return render(request, "videoclub/forbidden.html", context)

def redirect_forbidden(request):
    if request.user.is_authenticated:
        return redirect("/videoclub/films")
    else:
        return redirect("/videoclub/login")