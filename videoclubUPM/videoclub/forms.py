from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.forms import ModelForm
from videoclub.models import Movie
from django import forms

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
    username = forms.CharField(required=True,label='Username',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    
    first_name = forms.CharField(required=False,label='First name',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    
    last_name = forms.CharField(required=False,label='Last name',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    email = forms.CharField(required=True,label='Email',widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    ))

    password = forms.CharField(label='Password',widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'hidden'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        help_texts = {
            'username': ''
        }

class EditPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True,label='Old password',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    new_password1 = forms.CharField(required=True,label='New password',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    new_password2 = forms.CharField(required=True,label='Confirm new password',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    class Meta:
        model = User

class EditFilmForm(ModelForm):
    overview = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Movie
        fields = ('title', 'original_title','overview', 'date', 'director',
                    'url_poster', 'vote_average', 'url_video', 'budget', 'revenue', 'original_language', 'status', 'runtime')