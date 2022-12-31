from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import CharacterSheet, AliasesSheet, Aliase
from carrieres.models import Carriere
from reputations.models import CommonReputation
from .forms import CharacterSheetForm
from reputations.forms import CommonReputationForm
from competences.models import Skill, SkillSheet
from competences.forms import SkillSheetForm
from equipement.models import Weapon, Armor, StuffSheet
from cartes.models import Card, CardSheet
from succes.models import Achievement, AchievementsSheet
from succes.forms import AchievementsheetForm
from utils.sheets import search_sheets, paginate_sheets
from utils.common import toJs, stuffToJs


@login_required(login_url='login')
def fiches(request, results):
    page_title = "Carrières Marbrume"
    carrieres = Carriere.objects.all()
    form = CharacterSheetForm()
    fiches, search_query = search_sheets(request, results)
    custom_range, fiches = paginate_sheets(request, fiches, 14)
    url = "https://www.marbrume.com/fiche/details/"
    context = {'page_title': page_title, 'fiches': fiches, 'carrieres': carrieres,
               'form': form, 'search_query': search_query, 'custom_range': custom_range, 'url': url, 'results': results}
    return render(request, 'fiches/fiches.html', context)


@login_required(login_url='login')
def fiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    form = CharacterSheetForm(instance=fiche)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)
    cards = CardSheet.objects.filter(owner_id=pk)
    repForm = CommonReputationForm(instance=reputation)
    skills = Skill.objects.all()
    sheets = SkillSheet.objects.filter(owner_id=pk)
    aliases = AliasesSheet.objects.get(owner_id=pk)

    sheetForms = []
    index = 0

    for skill in sheets:
        sheetForm = SkillSheetForm(instance=sheets[index])
        setattr(sheetForm, 'id', skill.id)
        setattr(sheetForm, 'name', skill.skill)
        sheetForms.append(sheetForm)
        index += 1

    stuffsheets = StuffSheet.objects.filter(owner_id=pk)

    achievements = AchievementsSheet.objects.get(owner_id=pk)
    achievementsForm = AchievementsheetForm(instance=achievements)
    achievementsList = Achievement.objects.all()

    fields = []

    for f in achievements._meta.get_fields(include_hidden=True):
        value = getattr(achievements, f.name)
        fields.append({'name': f.name,
                       'value': value,
                       })

    fieldList = fields[2:92]

    for i, achievement in enumerate(achievementsList):
        fieldList[i]['text'] = achievement.text
        fieldList[i]['id'] = achievement.id

    skill_list = toJs(Skill, "name")
    alias_list = toJs(Aliase, "owner__name")
    card_list = toJs(Card, "ref__name")
    stuff_list = stuffToJs(Weapon, Armor, "name")

    page_title = f"Carrière {fiche.name}"
    url = "https://www.marbrume.com/fiche/details/"
    rurl = "https://www.marbrume.com/reputations/details/"
    murl = "https://www.marbrume.com/fiche/model/iframe/"

    context = {'page_title': page_title,
               'fiche': fiche, 'form': form, 'skills': skills,
               'skill_list': skill_list, 'stuff_list': stuff_list,
               'alias_list': alias_list, 'card_list': card_list,
               'sheetForms': sheetForms, 'stuffsheets': stuffsheets,
               'repForm': repForm, 'carriere': carriere, 'reputation': reputation,
               'cards': cards, 'aliases': aliases,
               'achievements': achievements, 'achievementsForm': achievementsForm,
               'fieldList': fieldList, 'achievementsList': achievementsList,
               'url': url, 'rurl': rurl, 'murl': murl}
    return render(request, 'fiches/fiche_details.html', context)


@login_required(login_url='login')
def addFiche(request):
    form = CharacterSheetForm()

    if request.method == "POST":

        form = CharacterSheetForm(request.POST, request.FILES)
        if form.is_valid():
            fiche = form.save(commit=False)
            fiche.group = fiche.path.group
            fiche.save()
            return redirect(f'/fiche/{fiche.id}')
        else:
            print(form.errors)

    return redirect('')


@login_required(login_url='login')
def editFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)

    if request.method == "POST":

        form = CharacterSheetForm(request.POST, request.FILES, instance=fiche)
        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


def ficheDetails(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)

    page_title = f"Carrière {fiche.name}"
    proxy = "https://www.marbrume.com"
    context = {'page_title': page_title, 'fiche': fiche,
               'carriere': carriere, 'proxy': proxy}
    return render(request, 'fiches/iframe.html', context)


def ficheModel(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)
    cards = CardSheet.objects.filter(owner_id=pk)
    sheets = SkillSheet.objects.filter(owner_id=pk)
    stuffsheets = StuffSheet.objects.filter(owner_id=pk)

    competences = []
    index = 0

    for skill in sheets:
        sheetItem = sheets[index]
        setattr(sheetItem, 'id', skill.id)
        setattr(sheetItem, 'name', skill.skill)
        competences.append(sheetItem)
        index += 1

    achievements = AchievementsSheet.objects.get(owner_id=pk)
    achievementsList = Achievement.objects.all()

    fields = []

    for f in achievements._meta.get_fields(include_hidden=True):
        value = getattr(achievements, f.name)
        fields.append({'name': f.name,
                       'value': value,
                       })

    fieldList = fields[2:92]

    for i, achievement in enumerate(achievementsList):
        fieldList[i]['text'] = achievement.text

    page_title = f"Carrière {fiche.name}"
    proxy = "https://www.marbrume.com"
    context = {'page_title': page_title, 'fiche': fiche, 'carriere': carriere, 'cards': cards,
               'reputation': reputation, 'competences': competences, 'stuffsheets': stuffsheets,
               'fieldList': fieldList, 'proxy': proxy}
    return render(request, 'fiches/modele.html', context)


def ficheModelIframe(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    carriere = Carriere.objects.get(name=fiche.path)
    reputation = CommonReputation.objects.get(owner_id=pk)
    cards = CardSheet.objects.filter(owner_id=pk)
    sheets = SkillSheet.objects.filter(owner_id=pk)
    stuffsheets = StuffSheet.objects.filter(owner_id=pk)
    competences = []
    index = 0

    for skill in sheets:
        sheetItem = sheets[index]
        setattr(sheetItem, 'id', skill.id)
        setattr(sheetItem, 'name', skill.skill)
        competences.append(sheetItem)
        index += 1

        achievements = AchievementsSheet.objects.get(owner_id=pk)
        achievementsList = Achievement.objects.all()

    fields = []

    for f in achievements._meta.get_fields(include_hidden=True):
        value = getattr(achievements, f.name)
        fields.append({'name': f.name,
                       'value': value,
                       })

    fieldList = fields[2:92]

    for i, achievement in enumerate(achievementsList):
        fieldList[i]['text'] = achievement.text

    page_title = f"Carrière {fiche.name}"
    proxy = "https://www.marbrume.com"
    context = {'page_title': page_title, 'fiche': fiche, 'carriere': carriere, 'cards': cards,
               'reputation': reputation, 'competences': competences,
               'stuffsheets': stuffsheets, 'fieldList': fieldList, 'proxy': proxy}
    return render(request, 'fiches/modele_iframe.html', context)


@login_required(login_url='login')
def delFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    fiche.delete()
    return redirect('/')


@login_required(login_url='login')
def confirmFiche(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "fiche"

    context = {'page_title': page_title, 'fiche': fiche, 'sender': sender}
    return render(request, 'base/confirm.html', context)
