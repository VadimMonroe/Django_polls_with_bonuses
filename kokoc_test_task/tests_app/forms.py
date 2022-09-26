from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             'placeholder': 'login'}))
    password1 = forms.CharField(label='Пароль1',
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'placeholder': 'password'}))
    password2 = forms.CharField(label='Пароль2',
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'placeholder': 'repeat the password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'login'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'placeholder': 'password'}))
