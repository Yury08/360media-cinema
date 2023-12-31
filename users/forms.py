from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'id': 'firstname'})
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'lastname'})
    )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'profile_field'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'profile_field'})
    )

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileImagesForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput  # Что бы убрать кнопку "Очистить"
    )

    class Meta:
        model = Profile
        fields = ['img']
