from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
import pytz
import pycountry


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


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Nazwa użytkownika')
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}),
                             label='Adres e-mail')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, label='Numer telefonu')
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False, label='Zdjęcie profilowe')
    website = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, label='Strona internetowa')
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False, label='Opis')

    class Meta:
        model = models.Profile
        fields = ['phone', 'avatar', 'website', 'bio']


class LocationForm(forms.ModelForm):
    country = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=[(name, name) for name in [country.name for country in pycountry.countries]]), required=False, label='Kraj')
    voivodeship = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=False, label='Województwo')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, label='Miejscowość')
    postcode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), min_value=0, max_value=99999, required=False, label='Kod pocztowy')
    time_zone = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=[(x, x) for x in pytz.common_timezones]), required=False, label='Strefa czasowa')
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=False, label='Ulica')
    street_no = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, label='Numer domu')
    house_no = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, label='Numer mieszkania')

    class Meta:
        model = models.Profile
        fields = ['country', 'time_zone', 'voivodeship', 'city', 'postcode', 'street', 'street_no', 'house_no']


class SensitiveForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), required=False, label='Data urodzenia')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, required=False, label='Imię')
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50, required=False, label='Nazwisko')
    gender = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=models.Profile.GENDER_CHOICES), required=False, label='Płeć')


    class Meta:
        model = models.Profile
        fields = ['name', 'surname', 'gender', 'birth_date']