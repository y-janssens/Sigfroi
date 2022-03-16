from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CharacterSheet
from carrieres.models import Carriere
from .forms import CharacterSheetForm
from .utils import searchFiche, paginateFiche

PROXY = "https://carrieres-marbrume.herokuapp.com"
URL = f"{PROXY}/fiches/details/"


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
            login(request, user)
            return redirect('/')

        else:
            messages.error(
                request, 'Le nom d\'utilisateur et/ou le mot de passe sont incorrects')
    return render(request, 'fiches/login.html', {'page_title': page_title})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


@login_required(login_url='login')
def fiches(request):
    page_title = "Carrières Marbrume"
    carrieres = Carriere.objects.all()
    form = CharacterSheetForm()
    fiches, search_query = searchFiche(request)
    custom_range, fiches = paginateFiche(request, fiches, 15)
    context = {'page_title': page_title, 'fiches': fiches, 'carrieres': carrieres,
               'form': form, 'search_query': search_query, 'custom_range': custom_range, 'url': URL}
    return render(request, 'fiches/list.html', context)


@login_required(login_url='login')
def fiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    form = CharacterSheetForm(instance=fiche)
    carriere = Carriere.objects.get(name=fiche.path)
    print(fiche.path)
    page_title = f"Carrière {fiche.name}"

    if request.method == "POST":
        form = CharacterSheetForm(request.POST)

        if form.is_valid():
            fiche = form.save(commit=False)
            fiche.save()
            return redirect('/')

    context = {'page_title': page_title,
               'fiche': fiche, 'form': form, 'carriere': carriere, 'proxy': PROXY, 'url': URL}
    return render(request, 'fiches/sheets.html', context)


@login_required(login_url='login')
def editFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    form = CharacterSheetForm(instance=fiche)

    if request.method == "POST":
        form = CharacterSheetForm(request.POST, instance=fiche)

        if form.is_valid():
            form.save()
            return redirect(f'/fiches/{fiche.id}')

    return redirect(f'/fiches/{fiche.id}')


def ficheDetails(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    page_title = f"Carrière {fiche.name}"
    context = {'page_title': page_title, 'fiche': fiche, 'proxy': PROXY}
    return render(request, 'fiches/details.html', context)


def addFiche(request):
    form = CharacterSheetForm()

    if request.method == "POST":
        form = CharacterSheetForm(request.POST)

        if form.is_valid():
            fiche = form.save(commit=False)
            fiche.save()
            return redirect('/')

    return redirect('/')


@login_required(login_url='login')
def delFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    fiche.delete()
    return redirect('/')


@login_required(login_url='login')
def confirm(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    page_title = "Confirmation"

    context = {'page_title': page_title, 'fiche': fiche}
    return render(request, 'fiches/confirm.html', context)
