from django.shortcuts import render, redirect
from .models import Carriere
from .forms import CareerForm
from .utils import searchCarriere, paginateCarriere

PROXY = "https://carrieres-marbrume.herokuapp.com"
URL = f"{PROXY}/carrieres/details/"


def carrieres(request):
    carrieres = Carriere.objects.all()
    form = CareerForm()
    carrieres, search_query = searchCarriere(request)
    custom_range, carrieres = paginateCarriere(request, carrieres, 15)
    context = {'carrieres': carrieres, 'form': form,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'carrieres/carrieres.html', context)


def carriere(request, pk):
    carriere = Carriere.objects.get(id=pk)
    form = CareerForm(instance=carriere)

    page_title = f"Carrière {carriere.name}"

    if request.method == "POST":
        form = CareerForm(request.POST)

        if form.is_valid():
            carriere = form.save(commit=False)
            carriere.save()
            return redirect('/carrieres')

    context = {'page_title': page_title, 'form': form,
               'carriere': carriere, 'proxy': PROXY, 'url': URL}
    return render(request, 'carrieres/carriere_details.html', context)


def addCarriere(request):
    form = CareerForm()

    if request.method == "POST":
        form = CareerForm(request.POST)

        if form.is_valid():
            carriere = form.save(commit=False)
            carriere.save()
            return redirect('/carrieres')

    return redirect('/carrieres')


def editCarriere(request, pk):
    carriere = Carriere.objects.get(id=pk)
    form = CareerForm(instance=carriere)

    if request.method == "POST":
        form = CareerForm(request.POST, instance=carriere)

        if form.is_valid():
            form.save()
            return redirect(f'/carrieres/{carriere.id}')

    return redirect(f'/carrieres/{carriere.id}')


def deleteCarriere(request, pk):
    carriere = Carriere.objects.get(id=pk)
    carriere.delete()
    return redirect('/carrieres')


def confirm(request, pk):
    carriere = Carriere.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "carrière"

    context = {'page_title': page_title,
               'carriere': carriere, 'sender': sender}
    return render(request, 'base/confirm.html', context)
