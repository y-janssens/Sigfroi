from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import *


def searchWeapon(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    weapons = Weapon.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(type__icontains=search_query)
    )

    return weapons, search_query


def searchArmor(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    armors = Armor.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(type__icontains=search_query) |
        Q(areas__icontains=search_query)
    )

    return armors, search_query


def paginateWeapon(request, weapons, results):
    page = request.GET.get('page')
    paginator = Paginator(weapons, results)

    try:
        weapons = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        weapons = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        weapons = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, weapons


def paginateArmor(request, weapons, results):
    page = request.GET.get('page')
    paginator = Paginator(weapons, results)

    try:
        weapons = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        weapons = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        weapons = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, weapons
