from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet
from .models import *
#from .utils import searchSkill, paginateSkill


@login_required(login_url='login')
def weapons(request):
    weapons = Weapon.objects.all()

    page_title = "Armurerie - armes"
    context = {'page_title': page_title,
               'weapons': weapons}
    return render(request, 'equipement/equipements.html', context)


@login_required(login_url='login')
def weapon(request, pk):
    weapon = Weapon.objects.get(id=pk)
    sender = 'weapon'
    page_title = weapon.name
    context = {'page_title': page_title,
               'weapon': weapon, 'sender': sender}
    return render(request, 'equipement/equipement.html', context)


@login_required(login_url='login')
def armors(request):
    armors = Armor.objects.all()

    page_title = "Armurerie - armures"
    context = {'armors': armors, 'page_title': page_title}
    return render(request, 'equipement/equipements.html', context)


@login_required(login_url='login')
def armor(request, pk):
    armor = Armor.objects.get(id=pk)
    sender = 'armor'
    page_title = armor.name
    context = {'armor': armor, 'page_title': page_title, 'sender': sender}
    return render(request, 'equipement/equipement.html', context)
