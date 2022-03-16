from django.shortcuts import render, redirect
from .models import Carriere
from .forms import CareerForm

PROXY = "https://carrieres-marbrume.herokuapp.com"
URL = f"{PROXY}/carrieres/details/"

def carrieres(request):
    carrieres = Carriere.objects.all()
    form = CareerForm()
    context = {'carrieres': carrieres, 'form': form}
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
            return redirect('carrieres/')

    context = {'page_title': page_title, 'form': form, 'carriere': carriere, 'proxy': PROXY, 'url': URL}
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
