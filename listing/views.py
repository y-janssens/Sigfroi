from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *
from fiches.forms import *

page_title = "Recensement des métiers et postes de nos joueurs"
fiches = CharacterSheet.objects.all()
latest = CharacterSheet.objects.first()
aliases = AliasesSheet.objects.all()

malesCount = CharacterSheet.objects.filter(
    gender="Homme").filter(is_active="Oui").count()
femalesCount = CharacterSheet.objects.filter(
    gender="Femme").filter(is_active="Oui").count()

noblesCount = CharacterSheet.objects.filter(
    group="Noble").filter(is_active="Oui").count()
noblesMalesCount = CharacterSheet.objects.filter(group="Noble").filter(
    gender="Homme").filter(is_active="Oui").count()
noblesFemalesCount = CharacterSheet.objects.filter(
    group="Noble").filter(gender="Femme").filter(is_active="Oui").count()

militiaCount = CharacterSheet.objects.filter(
    group="Milice(ne)").filter(is_active="Oui").count()
militiaMalesCount = CharacterSheet.objects.filter(group="Milice(ne)").filter(
    gender="Homme").filter(is_active="Oui").count()
militiaFemalesCount = CharacterSheet.objects.filter(
    group="Milice(ne)").filter(gender="Femme").filter(is_active="Oui").count()

peopleCount = CharacterSheet.objects.filter(
    group="Habitant(e)").filter(is_active="Oui").count()
peopleMalesCount = CharacterSheet.objects.filter(group="Habitant(e)").filter(
    gender="Homme").filter(is_active="Oui").count()
peopleFemalesCount = CharacterSheet.objects.filter(
    group="Habitant(e)").filter(gender="Femme").filter(is_active="Oui").count()

clergyCount = CharacterSheet.objects.filter(
    group="Prêtre(sse)").filter(is_active="Oui").count()
clergyMalesCount = CharacterSheet.objects.filter(group="Prêtre(sse)").filter(
    gender="Homme").filter(is_active="Oui").count()
clergyFemalesCount = CharacterSheet.objects.filter(
    group="Prêtre(sse)").filter(gender="Femme").filter(is_active="Oui").count()

banishedCount = CharacterSheet.objects.filter(
    group="Banni(e)").filter(is_active="Oui").count()
banishedMalesCount = CharacterSheet.objects.filter(
    group="Banni(e)").filter(gender="Homme").filter(is_active="Oui").count()
banishedFemalesCount = CharacterSheet.objects.filter(
    group="Banni(e)").filter(gender="Femme").filter(is_active="Oui").count()


@login_required(login_url='login')
def listing(request):
    proxy = f"https://www.marbrume.com/listing/iframe"
    owners = []
    owned = []
    ownedMales = []
    ownedFemales = []

    for i in aliases.all():
        if(len(i.aliases.all()) > 0):
            owners.append(i)
        for z in i.aliases.all():
            if(z.owner.gender == "Homme"):
                ownedMales.append(z)
            elif(z.owner.gender == "Femme"):
                ownedFemales.append(z)
            owned.append(z)

    ownerList = len(owners)
    aliasList = len(owned)
    aliasMales = len(ownedMales)
    aliasFemales = len(ownedFemales)

    context = {'page_title': page_title, 'fiches': fiches, 'latest': latest, 'aliases': aliases, 'ownerList': ownerList, 'aliasList': aliasList, 'aliasMales': aliasMales, 'aliasFemales': aliasFemales, 'noblesCount': noblesCount, 'noblesMalesCount': noblesMalesCount, 'noblesFemalesCount': noblesFemalesCount, 'militiaCount': militiaCount, 'militiaMalesCount': militiaMalesCount, 'militiaFemalesCount': militiaFemalesCount, 'peopleCount': peopleCount, 'peopleMalesCount': peopleMalesCount,
               'peopleFemalesCount': peopleFemalesCount, 'clergyCount': clergyCount, 'clergyMalesCount': clergyMalesCount, 'clergyFemalesCount': clergyFemalesCount, 'banishedCount': banishedCount, 'banishedMalesCount': banishedMalesCount, 'banishedFemalesCount': banishedFemalesCount, 'malesCount': malesCount, 'femalesCount': femalesCount, 'proxy': proxy}

    return render(request, 'listing/listing.html', context)


def listingIframe(request):
    context = {'page_title': page_title, 'fiches': fiches, 'latest': latest, 'aliases': aliases, 'noblesCount': noblesCount, 'noblesMalesCount': noblesMalesCount, 'noblesFemalesCount': noblesFemalesCount, 'militiaCount': militiaCount, 'militiaMalesCount': militiaMalesCount, 'militiaFemalesCount': militiaFemalesCount, 'peopleCount': peopleCount,
               'peopleMalesCount': peopleMalesCount, 'peopleFemalesCount': peopleFemalesCount, 'clergyCount': clergyCount, 'clergyMalesCount': clergyMalesCount, 'clergyFemalesCount': clergyFemalesCount, 'banishedCount': banishedCount, 'banishedMalesCount': banishedMalesCount, 'banishedFemalesCount': banishedFemalesCount, 'malesCount': malesCount, 'femalesCount': femalesCount}
    return render(request, 'listing/listing_iframe.html', context)


@login_required(login_url='login')
def addAliasSheet(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    alias = AliasesSheet.objects.get(owner_id=pk)

    if request.method == "POST":
        for i in request.POST.getlist('send-aliases'):
            alias.aliases.add(Aliase.objects.get(owner__name=i))
        return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


@login_required(login_url='login')
def confirmAliasSheet(request, pk, slug):
    alias = AliasesSheet.objects.get(owner_id=pk)
    ref = Aliase.objects.get(owner__name=slug)
    page_title = "Confirmation"
    sender = "aliasSheet"

    context = {'page_title': page_title,
               'alias': alias, 'ref': ref, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteAliasSheet(request, pk, slug):
    fiche = CharacterSheet.objects.get(id=pk)
    alias = AliasesSheet.objects.get(owner_id=pk)

    alias.aliases.remove(Aliase.objects.get(owner__name=slug))
    return redirect(f'/fiche/{fiche.id}')
