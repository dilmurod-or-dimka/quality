from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']