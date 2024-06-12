from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, UserForm, ProfileForm, LocationForm, SensitiveForm
from django.contrib.auth.decorators import login_required


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile')
        
        form = LoginForm()
        return render(request,'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Zalogowano pomyślnie. Witaj { request.user.username }!')
                return redirect('profile')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Nieprawidłowa nazwa użytkownika lub hasło.')
        return render(request,'users/login.html',{'form': form})


def sign_out(request):
    logout(request)
    messages.success(request,f'Wylogowano pomyślnie.')
    return redirect('login')


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Zarejestrowano pomyślnie.')
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'users/register.html', {'form': form})


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile)
        sensitive_form = SensitiveForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid() and sensitive_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            sensitive_form.save()
            messages.success(request, 'Twój profil został zaktualizowany.')
            return redirect('profile')
        else:
            messages.error(request, 'Coś poszło nie tak. Popraw informacje i spróbuj ponownie.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile)
        sensitive_form = SensitiveForm(request.POST, instance=request.user.profile)
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'location_form': location_form,
        'sensitive_form': sensitive_form
    })