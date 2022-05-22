from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *

@login_required(login_url='login')
def listing(request):
    page_title = "Recensement des métiers et postes de nos joueurs"
    fiches = CharacterSheet.objects.all()
    latest = CharacterSheet.objects.first() 
    aliases = AliasesSheet.objects.all()

    malesCount= CharacterSheet.objects.filter(gender="Homme").count()
    femalesCount= CharacterSheet.objects.filter(gender="Femme").count()

    noblesCount = CharacterSheet.objects.filter(group="Noble").count()
    noblesMalesCount = CharacterSheet.objects.filter(group="Noble").filter(gender="Homme").count()
    noblesFemalesCount = CharacterSheet.objects.filter(group="Noble").filter(gender="Femme").count()

    militiaCount = CharacterSheet.objects.filter(group="Milice(ne)").count()
    militiaMalesCount = CharacterSheet.objects.filter(group="Milice(ne)").filter(gender="Homme").count()
    militiaFemalesCount = CharacterSheet.objects.filter(group="Milice(ne)").filter(gender="Femme").count()

    peopleCount = CharacterSheet.objects.filter(group="Habitant(e)").count()
    peopleMalesCount = CharacterSheet.objects.filter(group="Habitant(e)").filter(gender="Homme").count()
    peopleFemalesCount = CharacterSheet.objects.filter(group="Habitant(e)").filter(gender="Femme").count()

    clergyCount = CharacterSheet.objects.filter(group="Prêtre(sse)").count()
    clergyMalesCount = CharacterSheet.objects.filter(group="Prêtre(sse)").filter(gender="Homme").count()
    clergyFemalesCount = CharacterSheet.objects.filter(group="Prêtre(sse)").filter(gender="Femme").count()

    banishedCount = CharacterSheet.objects.filter(group="Banni(e)").count()
    banishedMalesCount = CharacterSheet.objects.filter(group="Banni(e)").filter(gender="Homme").count()
    banishedFemalesCount = CharacterSheet.objects.filter(group="Banni(e)").filter(gender="Femme").count()
    
    proxy = f"{request.scheme}://{request.META['HTTP_HOST']}/listing/iframe"

    context = {'page_title': page_title, 'fiches': fiches, 'latest': latest, 'aliases': aliases, 'noblesCount': noblesCount, 'noblesMalesCount': noblesMalesCount, 'noblesFemalesCount': noblesFemalesCount, 'militiaCount': militiaCount, 'militiaMalesCount': militiaMalesCount, 'militiaFemalesCount': militiaFemalesCount, 'peopleCount': peopleCount, 'peopleMalesCount': peopleMalesCount, 'peopleFemalesCount': peopleFemalesCount, 'clergyCount': clergyCount, 'clergyMalesCount': clergyMalesCount, 'clergyFemalesCount': clergyFemalesCount, 'banishedCount': banishedCount, 'banishedMalesCount': banishedMalesCount, 'banishedFemalesCount': banishedFemalesCount, 'malesCount': malesCount, 'femalesCount': femalesCount, 'proxy': proxy}
    return render(request, 'listing/listing.html', context)

def listingIframe(request):
    page_title = "Recensement des métiers et postes de nos joueurs"
    fiches = CharacterSheet.objects.all()
    
    aliases = AliasesSheet.objects.all()
    latest = CharacterSheet.objects.last()

    context = {'page_title': page_title, 'fiches': fiches, 'aliases': aliases, 'latest': latest}
    return render(request, 'listing/listing_iframe.html', context)