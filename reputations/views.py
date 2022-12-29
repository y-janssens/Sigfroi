from django.shortcuts import render, redirect
from utils.decorators import login_required
from fiches.models import CharacterSheet
from .models import CommonReputation
from .forms import CommonReputationForm
from utils.reputations import flavorText


@login_required(login_url='login')
def editReputation(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)

    if request.method == "POST":

        reputation = CommonReputation.objects.get(owner_id=pk)
        form = CommonReputationForm(request.POST, instance=reputation)

        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


def reputationsDetails(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    reputation = CommonReputation.objects.get(owner_id=pk)

    page_title = f"Réputations {fiche.name}"

    context = {'page_title': page_title,
               'fiche': fiche, 'reputation': reputation, 'flavorText': flavorText}
    return render(request, 'reputations/iframe.html', context)
