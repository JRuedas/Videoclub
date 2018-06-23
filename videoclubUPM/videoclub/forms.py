from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from videoclub.models import Movie

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')
        help_texts = {
            'username': '',
            'password2': '',
            'is_staff': '',
        }

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_staff')
        help_texts = {
            'username': '',
            'is_staff': '',
        }

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        help_texts = {
            'username': ''
        }

class EditFilmForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'original_title','overview', 'date', 'director',
                    'url_poster', 'vote_average', 'url_video', 'budget', 'revenue', 'original_language', 'status', 'runtime')