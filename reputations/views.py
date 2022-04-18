from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet
from .models import PeopleReputation, MilitiaReputation, NobilityReputation, ClergyReputation, BanishedReputation
from .forms import *


@login_required(login_url='login')
def editReputation(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)

    if request.method == "POST":
        if fiche.group == 'Habitant(e)':
            reputation = PeopleReputation.objects.get(owner_id=pk)
            form = PeopleReputationForm(request.POST, instance=reputation)
        elif fiche.group == 'Milice(ne)':
            reputation = MilitiaReputation.objects.get(owner_id=pk)
            form = MilitiaReputationForm(request.POST, instance=reputation)
        elif fiche.group == 'Noble':
            reputation = NobilityReputation.objects.get(owner_id=pk)
            form = NobilityReputationForm(request.POST, instance=reputation)
        elif fiche.group == 'Prêtre(sse)':
            reputation = ClergyReputation.objects.get(owner_id=pk)
            form = ClergyReputationForm(request.POST, instance=reputation)
        elif fiche.group == 'Banni(e)':
            reputation = BanishedReputation.objects.get(owner_id=pk)
            form = BanishedReputationForm(request.POST, instance=reputation)

        if form.is_valid():
            form.save()
            return redirect(f'/fiches/fiche/{fiche.id}')

    return redirect(f'/fiches/fiche/{fiche.id}')
