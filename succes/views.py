from django.shortcuts import render, redirect
from decorators import login_required
from .models import *
from fiches.models import *
from .text import *

def success(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    succes = AchievementsSheet.objects.get(owner_id=pk)
    flavorText = achievementsList

    context = {'fiche': fiche, 'succes': succes, 'flavorText': flavorText}
    return render(request, 'succes/succes_block.html', context)