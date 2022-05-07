from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet
from .models import *
from .forms import *
from .text import flavorText

@login_required(login_url='login')
def editReputation(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)

    if request.method == "POST":
        
        reputation = CommonReputation.objects.get(owner_id=pk)
        form = CommonReputationForm(request.POST, instance=reputation)

        if form.is_valid():
            form.save()
            return redirect(f'/fiches/fiche/{fiche.id}')

    return redirect(f'/fiches/fiche/{fiche.id}')
