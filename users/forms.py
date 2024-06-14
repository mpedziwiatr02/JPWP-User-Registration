from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
import pytz
import pycountry


class LoginForm(forms.Form):
    # Formularz logowania z polami nazwa użytkownika i hasło
    username = forms.CharField(max_length=64, label="Nazwa użytkownika")
    password = forms.CharField(
        max_length=128, widget=forms.PasswordInput, label="Hasło"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dodanie klasy CSS do wszystkich widocznych pól formularza
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class RegisterForm(UserCreationForm):
    class Meta:
        # Model użytkownika oraz pola uwzględnione w formularzu rejestracji
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dodanie klasy CSS do wszystkich widocznych pól formularza
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class UserForm(forms.ModelForm):
    class Meta:
        # Model użytkownika oraz pola uwzględnione w formularzu edycji użytkownika
        model = User
        fields = ["username", "email"]

    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Nazwa użytkownika",
    )
    email = forms.EmailField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Adres e-mail",
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        # Model profilu oraz pola uwzględnione w formularzu edycji profilu
        model = models.Profile
        fields = ["phone", "avatar", "website", "bio"]

    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=32,
        required=False,
        label="Numer telefonu",
    )
    avatar = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
        label="Zdjęcie profilowe",
    )
    website = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=128,
        required=False,
        label="Strona internetowa",
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        max_length=512,
        required=False,
        label="Opis",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Zmiana etykiet w polu avatar
        self.fields["avatar"].widget.clear_checkbox_label = "Usuń"
        self.fields["avatar"].widget.initial_text = ""


class LocationForm(forms.ModelForm):
    class Meta:
        # Model profilu oraz pola uwzględnione w formularzu lokalizacji
        model = models.Profile
        fields = [
            "country",
            "time_zone",
            "region",
            "city",
            "postcode",
            "street",
            "street_no",
            "house_no",
        ]

    country = forms.CharField(
        widget=forms.Select(
            attrs={"class": "form-control", "id": "id-country"},
            choices=[
                (name, name)
                for name in [country.name for country in pycountry.countries]
            ],
        ),
        max_length=64,
        required=False,
        label="Kraj",
    )
    region = forms.CharField(
        widget=forms.Select(attrs={"class": "form-control", "id": "id-region"}),
        max_length=64,
        required=False,
        label="Region",
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=64,
        required=False,
        label="Miejscowość",
    )
    postcode = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=16,
        required=False,
        label="Kod pocztowy",
    )
    time_zone = forms.CharField(
        widget=forms.Select(
            attrs={"class": "form-control"},
            choices=[(x, x) for x in pytz.common_timezones],
        ),
        max_length=64,
        required=False,
        label="Strefa czasowa",
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=64,
        required=False,
        label="Ulica",
    )
    street_no = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=8,
        required=False,
        label="Dom",
    )
    house_no = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=8,
        required=False,
        label="Mieszkanie",
    )


class SensitiveForm(forms.ModelForm):
    class Meta:
        # Model profilu oraz pola uwzględnione w formularzu danych wrażliwych
        model = models.Profile
        fields = ["name", "surname", "gender", "birth_date"]

    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"
        ),
        required=False,
        label="Data urodzenia",
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=50,
        required=False,
        label="Imię",
    )
    surname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=50,
        required=False,
        label="Nazwisko",
    )
    gender = forms.CharField(
        widget=forms.Select(
            attrs={"class": "form-control"}, choices=models.Profile.GENDER_CHOICES
        ),
        required=False,
        label="Płeć",
    )
