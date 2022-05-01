from django.shortcuts import render, redirect
from decorators import login_required
from .models import CharacterSheet
from carrieres.models import Carriere
from reputations.models import *
from .forms import CharacterSheetForm
from reputations.forms import *
from competences.models import *
from .utils import searchFiche, paginateFiche
from reputations.text import flavorText

PROXY = "https://carrieres-marbrume.herokuapp.com"
URL = f"{PROXY}/fiches/fiche/details/"
RURL = f"{PROXY}/reputations/details/"


@login_required(login_url='login')
def fiches(request):
    page_title = "Carrières Marbrume"
    carrieres = Carriere.objects.all()
    form = CharacterSheetForm()
    fiches, search_query = searchFiche(request)
    custom_range, fiches = paginateFiche(request, fiches, 15)
    context = {'page_title': page_title, 'fiches': fiches, 'carrieres': carrieres,
               'form': form, 'search_query': search_query, 'custom_range': custom_range, 'url': URL}
    return render(request, 'fiches/fiches.html', context)


@login_required(login_url='login')
def fiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    form = CharacterSheetForm(instance=fiche)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)
    repForm = CommonReputationForm(instance=reputation)
    sheets = SkillSheet.objects.filter(owner_id=pk)

    page_title = f"Carrière {fiche.name}"    

    context = {'page_title': page_title,
               'fiche': fiche, 'form': form, 'sheets': sheets, 'repForm': repForm, 'carriere': carriere, 'reputation': reputation, 'flavorText': flavorText, 'url': URL, 'rurl': RURL}
    return render(request, 'fiches/fiche_details.html', context)


@login_required(login_url='login')
def editFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)

    if request.method == "POST":
        form = CharacterSheetForm(request.POST, instance=fiche)

        if form.is_valid():
            form.save()
            return redirect(f'/fiches/fiche/{fiche.id}')

    return redirect(f'/fiches/fiche/{fiche.id}')


def ficheDetails(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)
    page_title = f"Carrière {fiche.name}"
    context = {'page_title': page_title, 'fiche': fiche,
               'carriere': carriere, 'proxy': PROXY}
    return render(request, 'fiches/iframe.html', context)


@login_required(login_url='login')
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
def confirmFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "fiche"

    context = {'page_title': page_title, 'fiche': fiche, 'sender': sender}
    return render(request, 'base/confirm.html', context)
