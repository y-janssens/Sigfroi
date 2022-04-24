from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm


def registerUser(request):
    page_title = "Création de compte"

    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.save()
        if user.is_active == True:
            user.is_active = False
        user.save()
        messages.success(request, 'Compte crée avec succès, en attente de validation par un administrateur!')
        return redirect('login')

    context = {'page_title': page_title, 'form': form}
    return render(request, 'users/register.html', context)


def loginUser(request):
    page_title = "Connexion"
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Le nom d\'utilisateur n\'existe pas')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user.is_staff)
            login(request, user)
            messages.info(request, f'Bienvenue {user.username}!')
            return redirect('/')

        else:
            messages.error(
                request, 'Le nom d\'utilisateur et/ou le mot de passe sont incorrects')
    return render(request, 'users/login.html', {'page_title': page_title})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


