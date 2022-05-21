from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *
from .models import *

@login_required(login_url='login')
def cards(request):
    cards = Card.objects.all()
    page_title = "Cartes à collectionner"
    context = {'page_title': page_title, 'cards': cards}
    return render(request, 'cartes/cartes.html', context)