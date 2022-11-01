from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Achievement


def searchAchievement(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    succes = Achievement.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(id__icontains=search_query)
    )

    return succes, search_query


def paginateAchievement(request, succes, results):
    page = request.GET.get('page')
    paginator = Paginator(succes, results)

    try:
        succes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        succes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        succes = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, succes
