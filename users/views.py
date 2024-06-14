from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import login, authenticate, logout
from .forms import (
    LoginForm,
    RegisterForm,
    UserForm,
    ProfileForm,
    LocationForm,
    SensitiveForm,
)
from django.contrib.auth.decorators import login_required, user_passes_test
import pycountry
import os


def root(request):
    # Przekierowanie do profilu użytkownika
    return redirect("profile")


def sign_in(request):
    # Widok logowania użytkownika
    if request.method == "GET":
        # Jeśli użytkownik jest już zalogowany, przekieruj go do profilu
        if request.user.is_authenticated:
            return redirect("profile")

        # Wyświetlenie formularza logowania
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    # Przetwarzanie formularza logowania
    elif request.method == "POST":
        form = LoginForm(request.POST)

        # Uwierzytelnianie użytkownika
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                # Logowanie użytkownika
                login(request, user)
                messages.success(
                    request, f"Zalogowano pomyślnie. Witaj { request.user.username }!"
                )
                return redirect("profile")

        # Formularz jest niepoprawny lub użytkownik nie został uwierzytelniony
        messages.error(request, f"Nieprawidłowa nazwa użytkownika lub hasło.")
        return render(request, "users/login.html", {"form": form})


def sign_out(request):
    # Wylogowanie użytkownika
    logout(request)
    messages.success(request, f"Wylogowano pomyślnie.")
    return redirect("login")


@user_passes_test(lambda u: u.is_anonymous)  # Widok dostępny tylko dla niezalogowanych
def register(request):
    # Widok rejestracji nowego użytkownika
    if request.method == "GET":
        # Wyświetlenie formularza rejestracji
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    if request.method == "POST":
        # Przetwarzanie formularza rejestracji
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Zapisanie nowego użytkownika, ale nie zapisujemy jeszcze do bazy danych
            user = form.save(commit=False)
            # Modyfikacja danych użytkownika przed zapisaniem
            user.username = user.username.lower()
            # Ostateczne zapisanie użytkownika do bazy danych
            user.save()
            messages.success(request, "Zarejestrowano pomyślnie.")
            # Automatyczne logowanie nowo zarejestrowanego użytkownika
            login(request, user)
            return redirect("profile")
        else:
            # Formularz rejestracji jest niepoprawny, wyświetlenie formularza z błędami
            return render(request, "users/register.html", {"form": form})


@login_required  # Widok dostępny tylko dla zalogowanych
@transaction.atomic  # Wszystkie operacje w funkcji będą wykonane jako jedna transakcja
def profile(request):
    # Wyświetlanie i aktualizacja profilu użytkownika
    if request.method == "POST":
        # Pobranie formularzy i przypisanie danych z POST
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        location_form = LocationForm(request.POST, instance=request.user.profile)
        sensitive_form = SensitiveForm(request.POST, instance=request.user.profile)
        if (
            user_form.is_valid()
            and profile_form.is_valid()
            and location_form.is_valid()
            and sensitive_form.is_valid()
        ):
            # Zapisanie danych z formularzy
            user_form.save()
            profile_form.save()
            location_form.save()
            sensitive_form.save()
            messages.success(request, "Twój profil został zaktualizowany.")
            return redirect("profile")
        else:
            # Formularze zawierają błędy, użytkownik musi poprawić informacje
            messages.error(
                request, "Coś poszło nie tak. Popraw informacje i spróbuj ponownie."
            )
    else:
        # Pobranie formularzy dla GET request
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile)
        sensitive_form = SensitiveForm(instance=request.user.profile)

    # Pobranie podziału na regiony według krajów (potrzebne do dynamicznej zmiany opcji w polu region)
    subdivisions_dict = {}
    for country in pycountry.countries:
        subdivisions = pycountry.subdivisions.get(country_code=country.alpha_2)
        subdivisions_dict[country.name] = [
            (subd.code, subd.name) for subd in subdivisions
        ]

    # Renderowanie szablonu 'profile.html' z kontekstem (formularzami i podziałem na regiony)
    return render(
        request,
        "users/profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "location_form": location_form,
            "sensitive_form": sensitive_form,
            "subdivisions_dict": subdivisions_dict,
        },
    )
