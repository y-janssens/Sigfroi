from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import Map
from .forms import MapForm
from utils.maps import search_maps, paginate_maps
from utils.common import fill_confirmation_dict
from api.maps.serializers import parseMapName


@login_required(login_url='login')
def maps(request):
    cartes, search_query = search_maps(request)
    custom_range, cartes = paginate_maps(request, cartes, 15)
    form = MapForm()
    page_title = "Cartes du Royaume"
    url = 'https://cartes.marbrume.com/'
    context = {'page_title': page_title, 'maps': cartes, 'url': url, 'form': form,
               'custom_range': custom_range, 'search_query': search_query}
    return render(request, 'maps/maps_block.html', context)


@login_required(login_url='login')
def add_map(request):
    form = MapForm()

    if request.method == "POST":

        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            map = form.save(commit=False)
            print(form.data['name'])
            map.url = parseMapName(form.data)
            map.save()
        else:
            print(form.errors)

    return redirect('/maps')


@login_required(login_url='login')
def confirm_map(request, pk):
    card = Map.objects.get(uuid=pk)
    context = fill_confirmation_dict(card.name, "delete_map", card.uuid)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def delete_map(request, pk):
    card = Map.objects.get(uuid=pk)
    card.delete()
    return redirect('/maps')
