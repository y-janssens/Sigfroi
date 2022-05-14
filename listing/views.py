from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import CharacterSheet

@login_required(login_url='login')
def listing(request):
    page_title = "Carrières Marbrume"
    fiches = CharacterSheet.objects.all()
    latest = CharacterSheet.objects.last()

    print(latest.created)

    context = {'page_title': page_title, 'fiches': fiches, 'latest': latest}
    return render(request, 'listing/listing.html', context)
