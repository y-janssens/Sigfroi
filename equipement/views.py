from django.shortcuts import render, redirect
from utils.decorators import login_required
from fiches.models import CharacterSheet
from .models import Armor, Weapon, StuffSheet, ArmoryWeaponsNote, CustomSheet
from .forms import WeaponForm, ArmorForm, StuffSheetForm, CustomSheetForm
from utils.stuff import search_armors, search_weapons, paginate_armors, paginate_weapons
from utils.common import fill_confirmation_dict


def armory(request):
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()
    notes = ArmoryWeaponsNote.objects.all()

    page_title = "Armurerie - Tableau"
    context = {'page_title': page_title,
               'weapons': weapons, 'armors': armors, 'notes': notes}
    return render(request, 'equipement/table.html', context)


def armoryIframe(request):
    weapons = Weapon.objects.all()
    armors = Armor.objects.all()
    notes = ArmoryWeaponsNote.objects.all()

    page_title = "Armurerie"
    context = {'page_title': page_title,
               'weapons': weapons, 'armors': armors, 'notes': notes}
    return render(request, 'equipement/table_iframe.html', context)


@login_required(login_url='login')
def weapons(request):
    weaponForm = WeaponForm()
    weapons, search_query = search_weapons(request)
    custom_range, weapons = paginate_weapons(request, weapons, 50)

    page_title = "Armurerie - armes"
    context = {'page_title': page_title,
               'weapons': weapons, 'weaponForm': weaponForm, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'equipement/equipements.html', context)


@login_required(login_url='login')
def armors(request):
    armorForm = ArmorForm()
    armors, search_query = search_armors(request)
    custom_range, armors = paginate_armors(request, armors, 50)

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
    context = fill_confirmation_dict(weapon.name, "delete_weapon", weapon.id)
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
    context = fill_confirmation_dict(armor.name, "delete_armor", armor.id)
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
    if stuff.weapon is None:
        item = stuff.armor
    else:
        item = stuff.weapon
    context = fill_confirmation_dict(item.name, "delete_stuffSheet", stuff.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteStuffSheet(request, pk):
    stuff = StuffSheet.objects.get(id=pk)
    stuff.delete()
    return redirect(f'/fiche/{stuff.owner.id}')


@login_required(login_url='login')
def addCustomSheet(request, pk):
    form = CustomSheetForm()
    fiche = CharacterSheet.objects.get(id=pk)
    if request.method == "POST":
        form = CustomSheetForm(request.POST)
        if form.is_valid():
            custom = form.save(commit=False)
            custom.owner = fiche
            custom.save()
        return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


@login_required(login_url='login')
def confirmCustomSheet(request, pk):
    custom = CustomSheet.objects.get(id=pk)
    context = fill_confirmation_dict(custom.name, "delete_customSheet", custom.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteCustomSheet(request, pk):
    custom = CustomSheet.objects.get(id=pk)
    custom.delete()
    return redirect(f'/fiche/{custom.owner.id}')
