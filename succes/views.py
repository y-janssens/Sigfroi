from django.shortcuts import render, redirect
from decorators import login_required
from .models import *
from fiches.models import *
from .text import *


def success(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    achievements = AchievementsSheet.objects.get(owner_id=pk)
    flavorText = achievementsList

    fields = []

    for f in achievements._meta.get_fields(include_hidden=True):
        value = getattr(achievements, f.name)
        fields.append({'name': f.name,
                       'value': value,
                       })

    fieldList = fields[2:92]

    for i, index in enumerate(achievementsList):
        fieldList[i]['text'] = achievementsList[i]['text']

    context = {'fiche': fiche, 'achievements': achievements,
               'fieldList': fieldList, 'flavorText': flavorText}
    return render(request, 'succes/succes_details.html', context)
