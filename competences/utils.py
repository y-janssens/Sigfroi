from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Skill


def searchSkill(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.distinct().filter(
        Q(name__icontains=search_query)
    )

    return skills, search_query


def paginateSkill(request, skills, results):
    page = request.GET.get('page')
    paginator = Paginator(skills, results)

    try:
        skills = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        skills = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        skills = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, skills
