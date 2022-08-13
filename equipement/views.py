from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *
from .models import *
from .forms import *
from .utils import *


def armory(request):
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()

    page_title = "Armurerie - Tableau"
    context = {'page_title': page_title,
               'weapons': weapons, 'armors': armors}
    return render(request, 'equipement/table.html', context)


def armoryIframe(request):
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()

    page_title = "Armurerie - Tableau"
    context = {'page_title': page_title,
               'weapons': weapons, 'armors': armors}
    return render(request, 'equipement/table_iframe.html', context)


@login_required(login_url='login')
def weapons(request):
    weaponForm = WeaponForm()
    weapons, search_query = searchWeapon(request)
    custom_range, weapons = paginateWeapon(request, weapons, 50)

    page_title = "Armurerie - armes"
    context = {'page_title': page_title,
               'weapons': weapons, 'weaponForm': weaponForm, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'equipement/equipements.html', context)


@login_required(login_url='login')
def armors(request):
    armorForm = ArmorForm()
    armors, search_query = searchArmor(request)
    custom_range, armors = paginateArmor(request, armors, 50)

    page_title = "Armurerie - armures"
    context = {'armors': armors, 'page_title': page_title, 'armorForm': armorForm,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'equipement/equipements.html', context)


@login_required(login_url='login')
def weapon(request, pk):
    weapon = Weapon.objects.get(id=pk)
    weaponForm = WeaponForm(instance=weapon)

    sender = 'weapon'
    page_title = weapon.name
    context = {'page_title': page_title,
               'weapon': weapon, 'sender': sender, 'weaponForm': weaponForm}
    return render(request, 'equipement/equipement.html', context)


@login_required(login_url='login')
def addWeapon(request):
    form = WeaponForm()

    if request.method == "POST":
        form = WeaponForm(request.POST)

        if form.is_valid():
            weapon = form.save(commit=False)
            weapon.save()
            return redirect('/equipements/armes')

    return redirect('/equipements/armes')


@login_required(login_url='login')
def editWeapon(request, pk):
    weapon = Weapon.objects.get(id=pk)
    form = WeaponForm(instance=weapon)

    if request.method == "POST":
        form = WeaponForm(request.POST, instance=weapon)

        if form.is_valid():
            form.save()
            return redirect(f'/equipements/armes/{weapon.id}')

    return redirect(f'/competences/{weapon.id}')


@login_required(login_url='login')
def deleteWeapon(request, pk):
    weapon = Weapon.objects.get(id=pk)
    weapon.delete()
    return redirect('/equipements/armes')


@login_required(login_url='login')
def confirmWeapon(request, pk):
    weapon = Weapon.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "weapon"

    context = {'page_title': page_title,
               'weapon': weapon, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def armor(request, pk):
    armor = Armor.objects.get(id=pk)
    armorForm = ArmorForm(instance=armor)
    sender = 'armor'
    page_title = armor.name
    context = {'armor': armor, 'page_title': page_title,
               'sender': sender, 'armorForm': armorForm}
    return render(request, 'equipement/equipement.html', context)


@login_required(login_url='login')
def addArmor(request):
    form = ArmorForm()

    if request.method == "POST":
        form = ArmorForm(request.POST)

        if form.is_valid():
            armor = form.save(commit=False)
            armor.save()
            return redirect('/equipements/armures')

    return redirect('/equipements/armures')


@login_required(login_url='login')
def editArmor(request, pk):
    armor = Armor.objects.get(id=pk)
    form = ArmorForm(instance=armor)

    if request.method == "POST":
        form = ArmorForm(request.POST, instance=armor)

        if form.is_valid():
            form.save()
            return redirect(f'/equipements/armures/{armor.id}')

    return redirect(f'/competences/{armor.id}')


@login_required(login_url='login')
def deleteArmor(request, pk):
    armor = Armor.objects.get(id=pk)
    armor.delete()
    return redirect('/equipements/armures')


@login_required(login_url='login')
def confirmArmor(request, pk):
    armor = Armor.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "armor"

    context = {'page_title': page_title,
               'armor': armor, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def addStuffSheet(request, pk):
    form = StuffSheetForm()
    fiche = CharacterSheet.objects.get(id=pk)
    if request.method == "POST":
        for i in request.POST.getlist('send-stuff'):
            form = StuffSheetForm(request.POST)
            if form.is_valid():
                stuff = form.save(commit=False)
                stuff.owner = fiche
                try:
                    stuff.weapon = Weapon.objects.get(name=i)
                except:
                    stuff.armor = Armor.objects.get(name=i)
                stuff.save()
        return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


@login_required(login_url='login')
def confirmStuffSheet(request, pk):
    stuff = StuffSheet.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "stuffSheet"

    context = {'page_title': page_title, 'stuff': stuff, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteStuffSheet(request, pk):
    stuff = StuffSheet.objects.get(id=pk)
    stuff.delete()
    return redirect(f'/fiche/{stuff.owner.id}')
