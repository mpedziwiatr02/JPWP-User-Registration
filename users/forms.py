from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label='Nazwa użytkownika')
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='Hasło')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Nazwa użytkownika')
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}),
                             label='Hasło')

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False, label='Zdjęcie profilowe')
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False, label='Opis')
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, label='Lokalizacja')
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), required=False, label='Data urodzenia')

    class Meta:
        model = models.Profile
        fields = ['avatar', 'bio', 'location', 'birth_date']
