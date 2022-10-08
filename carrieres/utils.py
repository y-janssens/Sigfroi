from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Carriere


def searchCarriere(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    carrieres = Carriere.objects.distinct().filter(
        Q(name__icontains=search_query)
    )

    return carrieres, search_query


def paginateCarriere(request, carrieres, results):
    page = request.GET.get('page')
    paginator = Paginator(carrieres, results)

    try:
        carrieres = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        carrieres = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        carrieres = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, carrieres
