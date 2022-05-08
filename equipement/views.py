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
    return render(request, 'equipement/weapons.html', context)


@login_required(login_url='login')
def armors(request):
    armors = Armor.objects.all()

    page_title = "Armurerie - armures"
    context = {'armors': armors, 'page_title': page_title}
    return render(request, 'equipement/armors.html', context)
