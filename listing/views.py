from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet

@login_required(login_url='login')
def listing(request):
    page_title = "Recensement des métiers et postes de nos joueurs"
    fiches = CharacterSheet.objects.all()
    latest = CharacterSheet.objects.last()

    proxy = f"{request.scheme}://{request.META['HTTP_HOST']}/listing/iframe"

    context = {'page_title': page_title, 'fiches': fiches, 'latest': latest, 'proxy': proxy}
    return render(request, 'listing/listing.html', context)

def listingIframe(request):
    page_title = "Recensement des métiers et postes de nos joueurs"
    fiches = CharacterSheet.objects.all()
    latest = CharacterSheet.objects.last()

    print(latest.created)

    context = {'page_title': page_title, 'fiches': fiches, 'latest': latest}
    return render(request, 'listing/listing_iframe.html', context)