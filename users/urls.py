from django.urls import path
from . import views


# Definicje ścieżek URL dla aplikacji
urlpatterns = [
    path("", views.root, name="root"),  # Ścieżka do strony głównej
    path("login/", views.sign_in, name="login"),  # Ścieżka do logowania
    path("logout/", views.sign_out, name="logout"),  # Ścieżka do wylogowania
    path("profile/", views.profile, name="profile"),  # Ścieżka do profilu użytkownika
    path("register/", views.register, name="register"),  # Ścieżka do rejestracji użytkownika
]
