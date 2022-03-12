from django.db.models import Q
from .models import CharacterSheet

def searchFiche(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    fiches = CharacterSheet.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(path__icontains=search_query) |
        Q(group__icontains=search_query)
        )

    return fiches, search_query