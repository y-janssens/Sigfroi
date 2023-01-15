from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from lineage.models import Family, Character


def search_characters(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    characters = Character.objects.distinct().filter(
        Q(first_name__icontains=search_query) |
        Q(last_name__icontains=search_query)
    )
    return characters, search_query


def search_trees(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    trees = Family.objects.distinct().filter(
        Q(head__first_name__icontains=search_query) |
        Q(head__last_name__icontains=search_query)
    )
    return trees, search_query


def paginate_characters(request, characters, results):
    page = request.GET.get('page')
    paginator = Paginator(characters, results)

    try:
        characters = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        characters = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        characters = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, characters


def paginate_trees(request, trees, results):
    page = request.GET.get('page')
    paginator = Paginator(trees, results)

    try:
        trees = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        trees = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        trees = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, trees
