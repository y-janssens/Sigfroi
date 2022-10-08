from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Card


def searchFiche(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    cartes = Card.objects.distinct().filter(
        Q(ref__name__icontains=search_query) |
        Q(ref__group__icontains=search_query)
    )

    return cartes, search_query


def paginateFiche(request, cartes, results):
    page = request.GET.get('page')
    paginator = Paginator(cartes, results)

    try:
        cartes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        cartes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        cartes = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, cartes
