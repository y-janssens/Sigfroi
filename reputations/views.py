from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet
from .models import PeopleReputation, MilitiaReputation, NobilityReputation, ClergyReputation, BanishedReputation


@login_required(login_url='login')
def reputations(request):
    peopleReputations = PeopleReputation.objects.all()
    militiaReputations = MilitiaReputation.objects.all()
    nobilityReputations = NobilityReputation.objects.all()
    clergyReputations = ClergyReputation.objects.all()
    banishedReputations = BanishedReputation.objects.all()

    reputations = [peopleReputations, militiaReputations,
                   nobilityReputations, clergyReputations, banishedReputations]

    context = {'reputations': reputations}
    return render(request, 'reputations/reputations.html', context)
