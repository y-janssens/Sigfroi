from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet

fiches_male = CharacterSheet.objects.filter(is_active=True).filter(gender="Homme").order_by('name')
fiches_female = CharacterSheet.objects.filter(is_active=True).filter(gender="Femme").order_by('name')
latest = CharacterSheet.objects.first()
context = {'fiches_male': fiches_male, 'fiches_female': fiches_female, 'latest': latest}

def avatars(request):
    return render(request, 'avatars/avatars.html', context)


def avatars_iframe(request):
    return render(request, 'avatars/avatars_iframe.html', context)