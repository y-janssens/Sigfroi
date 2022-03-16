from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import CharacterSheet

def searchFiche(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    fiches = CharacterSheet.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        #Q(path__icontains=search_query) |
        Q(group__icontains=search_query) |
        Q(rank__icontains=search_query)
        )

    return fiches, search_query

def paginateFiche(request, fiches, results):
    page = request.GET.get('page')
    paginator = Paginator(fiches, results)
    
    try:
        fiches = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        fiches = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        fiches = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex >  paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, fiches