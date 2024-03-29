from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import Carriere
from .forms import CareerForm
from utils.path import searchCarriere, paginateCarriere
from utils.common import fill_confirmation_dict


@login_required(login_url='login')
def carrieres(request):
    carrieres = Carriere.objects.all()
    form = CareerForm()
    carrieres, search_query = searchCarriere(request)
    custom_range, carrieres = paginateCarriere(request, carrieres, 12)
    page_title = "Carrières"
    context = {'page_title': page_title, 'carrieres': carrieres,
               'search_query': search_query, 'custom_range': custom_range, 'form': form, 'range': range(4)}
    return render(request, 'carrieres/carrieres.html', context)


@login_required(login_url='login')
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

    proxy = "https://www.marbrume.com/carrieres/details"

    context = {'page_title': page_title, 'form': form,
               'carriere': carriere, 'proxy': proxy, 'range': range(4)}
    return render(request, 'carrieres/carriere_details.html', context)


@login_required(login_url='login')
def addCarriere(request):
    form = CareerForm()

    if request.method == "POST":
        form = CareerForm(request.POST)

        if form.is_valid():
            carriere = form.save(commit=False)
            carriere.save()
            return redirect('/carrieres')

    return redirect('/carrieres')


@login_required(login_url='login')
def editCarriere(request, pk):
    carriere = Carriere.objects.get(id=pk)
    form = CareerForm(instance=carriere)

    if request.method == "POST":
        form = CareerForm(request.POST, instance=carriere)

        if form.is_valid():
            form.save()
            return redirect(f'/carrieres/{carriere.id}')

    return redirect(f'/carrieres/{carriere.id}')


@login_required(login_url='login')
def deleteCarriere(request, pk):
    carriere = Carriere.objects.get(id=pk)
    carriere.delete()
    return redirect('/carrieres')


@login_required(login_url='login')
def confirmCarriere(request, pk):
    carriere = Carriere.objects.get(id=pk)
    context = fill_confirmation_dict(carriere.name, "delete_carriere", carriere.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def carrieresDetails(request):
    carrieres = Carriere.objects.all()
    page_title = "Carrières"
    shurl = "https://www.marbrume.com/carrieres/details/iframe"
    context = {'page_title': page_title,
               'carrieres': carrieres, 'shurl': shurl}
    return render(request, 'carrieres/carrieres_details.html', context)


def carrieresIframe(request):
    carrieres = Carriere.objects.all()
    page_title = "Carrières"
    context = {'page_title': page_title, 'carrieres': carrieres}
    return render(request, 'carrieres/carrieres_iframe.html', context)
