from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *

page_title = "Recensement des métiers et postes de nos joueurs"
fiches = CharacterSheet.objects.all()
latest = CharacterSheet.objects.first() 
aliases = AliasesSheet.objects.all()

malesCount= CharacterSheet.objects.filter(gender="Homme").filter(is_active="Oui").count()
femalesCount= CharacterSheet.objects.filter(gender="Femme").filter(is_active="Oui").count()

noblesCount = CharacterSheet.objects.filter(group="Noble").filter(is_active="Oui").count()
noblesMalesCount = CharacterSheet.objects.filter(group="Noble").filter(gender="Homme").filter(is_active="Oui").count()
noblesFemalesCount = CharacterSheet.objects.filter(group="Noble").filter(gender="Femme").filter(is_active="Oui").count()

militiaCount = CharacterSheet.objects.filter(group="Milice(ne)").filter(is_active="Oui").count()
militiaMalesCount = CharacterSheet.objects.filter(group="Milice(ne)").filter(gender="Homme").filter(is_active="Oui").count()
militiaFemalesCount = CharacterSheet.objects.filter(group="Milice(ne)").filter(gender="Femme").filter(is_active="Oui").count()

peopleCount = CharacterSheet.objects.filter(group="Habitant(e)").filter(is_active="Oui").count()
peopleMalesCount = CharacterSheet.objects.filter(group="Habitant(e)").filter(gender="Homme").filter(is_active="Oui").count()
peopleFemalesCount = CharacterSheet.objects.filter(group="Habitant(e)").filter(gender="Femme").filter(is_active="Oui").count()

clergyCount = CharacterSheet.objects.filter(group="Prêtre(sse)").filter(is_active="Oui").count()
clergyMalesCount = CharacterSheet.objects.filter(group="Prêtre(sse)").filter(gender="Homme").filter(is_active="Oui").count()
clergyFemalesCount = CharacterSheet.objects.filter(group="Prêtre(sse)").filter(gender="Femme").filter(is_active="Oui").count()

banishedCount = CharacterSheet.objects.filter(group="Banni(e)").filter(is_active="Oui").count()
banishedMalesCount = CharacterSheet.objects.filter(group="Banni(e)").filter(gender="Homme").filter(is_active="Oui").count()
banishedFemalesCount = CharacterSheet.objects.filter(group="Banni(e)").filter(gender="Femme").filter(is_active="Oui").count()

fullContext = {'page_title': page_title, 'fiches': fiches, 'latest': latest, 'aliases': aliases, 'noblesCount': noblesCount, 'noblesMalesCount': noblesMalesCount, 'noblesFemalesCount': noblesFemalesCount, 'militiaCount': militiaCount, 'militiaMalesCount': militiaMalesCount, 'militiaFemalesCount': militiaFemalesCount, 'peopleCount': peopleCount, 'peopleMalesCount': peopleMalesCount, 'peopleFemalesCount': peopleFemalesCount, 'clergyCount': clergyCount, 'clergyMalesCount': clergyMalesCount, 'clergyFemalesCount': clergyFemalesCount, 'banishedCount': banishedCount, 'banishedMalesCount': banishedMalesCount, 'banishedFemalesCount': banishedFemalesCount, 'malesCount': malesCount, 'femalesCount': femalesCount}

@login_required(login_url='login')
def listing(request):
    context = fullContext
    proxy = f"{request.scheme}://{request.META['HTTP_HOST']}/listing/iframe"
    setattr(context, "proxy", proxy )
    
    return render(request, 'listing/listing.html', context)

def listingIframe(request):
    context = fullContext
    return render(request, 'listing/listing_iframe.html', context)