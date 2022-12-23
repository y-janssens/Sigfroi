from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet, AliasesSheet, Aliase
from .models import Pantheon, PantheonCustom
from .forms import PantheonForm
from utils import list_to_js


def get_context():
    page_title = "Recensement des métiers et postes de nos joueurs"

    fiches = CharacterSheet.objects.all().filter(
        is_active=True).extra(order_by=['name'])
    latest = CharacterSheet.objects.first()
    aliases = AliasesSheet.objects.all().filter(owner__is_active=True)

    malesCount = CharacterSheet.objects.all().filter(
        gender="Homme").filter(is_active=True).count()
    femalesCount = CharacterSheet.objects.all().filter(
        gender="Femme").filter(is_active=True).count()

    noblesCount = CharacterSheet.objects.all().filter(
        group="Noble").filter(is_active=True).count()
    noblesMalesCount = CharacterSheet.objects.all().filter(group="Noble").filter(
        gender="Homme").filter(is_active=True).count()
    noblesFemalesCount = CharacterSheet.objects.all().filter(
        group="Noble").filter(gender="Femme").filter(is_active=True).count()

    militiaCount = CharacterSheet.objects.all().filter(
        group="Milice(ne)").filter(is_active=True).count()
    militiaMalesCount = CharacterSheet.objects.all().filter(group="Milice(ne)").filter(
        gender="Homme").filter(is_active=True).count()
    militiaFemalesCount = CharacterSheet.objects.all().filter(
        group="Milice(ne)").filter(gender="Femme").filter(is_active=True).count()

    peopleCount = CharacterSheet.objects.all().filter(
        group="Habitant(e)").filter(is_active=True).count()
    peopleMalesCount = CharacterSheet.objects.all().filter(group="Habitant(e)").filter(
        gender="Homme").filter(is_active=True).count()
    peopleFemalesCount = CharacterSheet.objects.all().filter(
        group="Habitant(e)").filter(gender="Femme").filter(is_active=True).count()

    clergyCount = CharacterSheet.objects.all().filter(
        group="Prêtre(sse)").filter(is_active=True).count()
    clergyMalesCount = CharacterSheet.objects.all().filter(group="Prêtre(sse)").filter(
        gender="Homme").filter(is_active=True).count()
    clergyFemalesCount = CharacterSheet.objects.all().filter(
        group="Prêtre(sse)").filter(gender="Femme").filter(is_active=True).count()

    banishedCount = CharacterSheet.objects.all().filter(
        group="Banni(e)").filter(is_active=True).count()
    banishedMalesCount = CharacterSheet.objects.all().filter(
        group="Banni(e)").filter(gender="Homme").filter(is_active=True).count()
    banishedFemalesCount = CharacterSheet.objects.all().filter(
        group="Banni(e)").filter(gender="Femme").filter(is_active=True).count()

    owners = []
    owned = []
    ownedMales = []
    ownedFemales = []

    for i in aliases.all():
        if (len(i.aliases.all()) > 0):
            owners.append(i)
        for z in i.aliases.all():
            if (z.owner.gender == "Homme"):
                ownedMales.append(z)
            else:
                ownedFemales.append(z)
            owned.append(z)

    ownerList = len(owners)
    aliasList = len(owned)
    aliasMales = len(ownedMales)
    aliasFemales = len(ownedFemales)

    proxy = "https://www.marbrume.com/listing/iframe"

    return {'page_title': page_title, 'fiches': fiches, 'latest': latest, 'aliases': aliases, 'ownerList': ownerList,
            'aliasList': aliasList, 'aliasMales': aliasMales, 'aliasFemales': aliasFemales, 'noblesCount': noblesCount,
            'noblesMalesCount': noblesMalesCount, 'noblesFemalesCount': noblesFemalesCount, 'militiaCount': militiaCount,
            'militiaMalesCount': militiaMalesCount, 'militiaFemalesCount': militiaFemalesCount, 'peopleCount': peopleCount,
            'peopleMalesCount': peopleMalesCount, 'peopleFemalesCount': peopleFemalesCount, 'clergyCount': clergyCount,
            'clergyMalesCount': clergyMalesCount, 'clergyFemalesCount': clergyFemalesCount, 'banishedCount': banishedCount,
            'banishedMalesCount': banishedMalesCount, 'banishedFemalesCount': banishedFemalesCount, 'malesCount': malesCount,
            'femalesCount': femalesCount, 'proxy': proxy}


@login_required(login_url='login')
def listing(request):
    context = get_context()
    return render(request, 'listing/listing.html', context)


def listingIframe(request):
    context = get_context()
    return render(request, 'listing/listing_iframe.html', context)


@login_required(login_url='login')
def addAliasSheet(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    alias = AliasesSheet.objects.get(owner_id=pk)

    if request.method == "POST":
        for i in request.POST.getlist('send-alias'):
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


@login_required(login_url='login')
def pantheon(request):
    page_title = "Panthéon"
    url = "https://marbrume.com/listing/pantheon/iframe/"
    form = PantheonForm()
    finishers = Pantheon.objects.all().order_by("id")
    customs = PantheonCustom.objects.all().order_by("id")
    finishers_list = list_to_js(Pantheon, "id", "name", "inscription_date", "completion_date")
    customs_list = list_to_js(PantheonCustom, "id", "name", "inscription_date", "completion_date")
    context = {"page_title": page_title, "finishers": finishers, "finishers_list": finishers_list,
               "customs": customs, "customs_list": customs_list, "url": url, 'form': form}
    return render(request, 'listing/pantheon/pantheon.html', context)


def pantheon_iframe(request):
    page_title = "Panthéon"
    finishers = Pantheon.objects.all().order_by("id")
    customs = PantheonCustom.objects.all().order_by("id")
    finishers_list = list_to_js(Pantheon, "id", "name", "inscription_date", "completion_date")
    customs_list = list_to_js(PantheonCustom, "id", "name", "inscription_date", "completion_date")
    context = {"page_title": page_title, "finishers": finishers, "finishers_list": finishers_list, "customs": customs, "customs_list": customs_list}
    context = {"page_title": page_title, "finishers": finishers, "finishers_list": finishers_list}
    return render(request, 'listing/pantheon/pantheon_iframe.html', context)


@login_required(login_url='login')
def addFinisher(request):
    form = PantheonForm()

    if request.method == "POST":

        form = PantheonForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/listing/pantheon/')


@login_required(login_url='login')
def confirmFinisher(request, pk):
    finisher = Pantheon.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "finisher"

    context = {'page_title': page_title, 'finisher': finisher, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteFinisher(request, pk):
    finisher = Pantheon.objects.get(id=pk)
    finisher.delete()
    return redirect('/listing/pantheon/')


@login_required(login_url='login')
def confirmCustom(request, pk):
    custom = PantheonCustom.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "custom"

    context = {'page_title': page_title, 'custom': custom, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteCustom(request, pk):
    customs = PantheonCustom.objects.get(id=pk)
    customs.delete()
    return redirect('/listing/pantheon/')
