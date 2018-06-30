from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.forms import ModelForm
from videoclub.models import Movie
from django import forms

class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True,label='Username',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    email = forms.CharField(required=True,label='Email',widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(required=True,label='Password',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(required=True,label='Confirm password',widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    is_staff = forms.BooleanField(required=False,label="Is admin?", widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')
        help_texts = {
            'username': '',
            'password2': '',
            'is_staff': '',
        }

class UserUpdateForm(UserChangeForm):
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

    is_staff = forms.BooleanField(required=False,label="Is admin?", widget=forms.CheckboxInput())

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
    title = forms.CharField(label='Title',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    original_title = forms.CharField(label='Original title',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    overview = forms.CharField(label='Overview',widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    date = forms.DateField(label='Release date',widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD'
        }
    ))

    director = forms.CharField(label='Director',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    url_poster = forms.CharField(label='URL Poster',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    vote_average = forms.DecimalField(label='Vote average',widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'step': 0.1,
            'min': '0.00',
            'max': '10.00'
        }
    ))

    url_video = forms.CharField(label='URL video',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    budget = forms.FloatField(label='Budget',widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ))

    revenue = forms.FloatField(label='Revenue',widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ))

    original_language = forms.CharField(label='Original language',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    status = forms.CharField(label='Status',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    runtime = forms.IntegerField(label='Rutime',widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Movie
        fields = ('title', 'original_title','overview', 'date', 'director',
                    'url_poster', 'vote_average', 'url_video', 'budget', 'revenue', 'original_language', 'status', 'runtime')