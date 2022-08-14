from django.shortcuts import render, redirect
from decorators import login_required
from .models import *
from .forms import *
from fiches.models import *


def Editsuccess(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    achievements = AchievementsSheet.objects.get(owner_id=pk)
    if request.method == "POST":
        form = AchievementsheetForm(request.POST, instance=achievements)
        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')
