from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from fiches.models import CharacterSheet


def search_sheets(request, active):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    fiches = CharacterSheet.objects.filter(is_active=active).distinct().filter(
        Q(name__icontains=search_query) |
        Q(path__name__icontains=search_query) |
        Q(group__icontains=search_query) |
        Q(rank__icontains=search_query)
    )
    return fiches, search_query


def search_sheets_details(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    fiche = CharacterSheet.objects.all().distinct().filter(
        Q(name__icontains=search_query) |
        Q(path__name__icontains=search_query) |
        Q(group__icontains=search_query) |
        Q(rank__icontains=search_query)
    ).first()
    print(search_query)
    if search_query != "":
        return redirect(f'/fiche/{fiche.id}')    
    return fiche, search_query


def paginate_sheets(request, fiches, results):
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
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, fiches
