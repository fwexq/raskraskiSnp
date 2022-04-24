from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, TextInput, Textarea, ImageField
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class pictureForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Ничего не выбрано'

    class Meta:
       model = picture
       fields = ['title', 'slug', 'description', 'image', 'cat', 'file']

       widgets = {
           "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
           "description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),

}




class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    capatcha = CaptchaField(label='Не робот:')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    capatcha = CaptchaField(label='Не робот:')
