from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *
from .models import *
from .forms import *
from .utils import *


@login_required(login_url='login')
def cards(request):
    cartes, search_query = searchFiche(request)
    custom_range, cartes = paginateFiche(request, cartes, 15)
    page_title = "Cartes à collectionner"
    context = {'page_title': page_title, 'cards': cartes, 'custom_range': custom_range, 'search_query': search_query}
    return render(request, 'cartes/cartes.html', context)


def addCardSheet(request, pk):
    form = CardSheetForm()
    fiche = CharacterSheet.objects.get(id=pk)
    if request.method == "POST":
        for i in request.POST.getlist('card-request'):
            form = CardSheetForm(request.POST)
            if form.is_valid():
                card = form.save(commit=False)
                card.owner = fiche
                card.card = Card.objects.get(
                    ref=CharacterSheet.objects.get(name=i))
                card.save()
        return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


@login_required(login_url='login')
def confirmCardSheet(request, pk):
    card = CardSheet.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "cardSheet"

    context = {'page_title': page_title, 'card': card, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteCardSheet(request, pk):
    card = CardSheet.objects.get(id=pk)
    card.delete()
    return redirect(f'/fiche/{card.owner.id}')
