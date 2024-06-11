from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]