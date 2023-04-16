from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from maps.models import Map


def search_maps(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    cartes = Map.objects.distinct().filter(name__icontains=search_query).order_by('created')

    return cartes, search_query


def paginate_maps(request, maps, results):
    page = request.GET.get('page')
    paginator = Paginator(maps, results)

    try:
        maps = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        maps = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        maps = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, maps
