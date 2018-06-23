from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


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