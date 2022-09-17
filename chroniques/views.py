from django.shortcuts import render, redirect
from decorators import login_required
from fiches.models import *
from .models import *
from .forms import *



noblesCount = CharacterSheet.objects.filter(
    group="Noble").filter(is_active="Oui").count()
militiaCount = CharacterSheet.objects.filter(
    group="Milice(ne)").filter(is_active="Oui").count()
peopleCount = CharacterSheet.objects.filter(
    group="Habitant(e)").filter(is_active="Oui").count()
clergyCount = CharacterSheet.objects.filter(
    group="Prêtre(sse)").filter(is_active="Oui").count()
banishedCount = CharacterSheet.objects.filter(
    group="Banni(e)").filter(is_active="Oui").count()



@login_required(login_url='login')
def chroniques(request):
    page_title = "Chroniques"
    chroniques = Chronique.objects.all()
    url = "https://www.marbrume.com/news/"
    context = {"page_title": page_title, "chroniques": chroniques, "url": url}
    return render(request, 'chroniques/chroniques.html', context)


def chronique(request, pk):
    chronique = Chronique.objects.get(id=pk)
    characters = CharacterSheet.objects.all().count()
    page_title = f"Chronique N°{chronique.id}"
    context = {"page_title": page_title, "chronique": chronique, "characters": characters, "noblesCount": noblesCount, "militiaCount": militiaCount, "clergyCount": clergyCount, "peopleCount": peopleCount, "banishedCount": banishedCount}
    return render(request, 'chroniques/chronique.html', context)


@login_required(login_url='login')
def newChronique(request):
    form = ChroniqueForm()
    page_title = "Nouvelle Chronique"
    context = {"page_title": page_title, "form": form}
    return render(request, 'chroniques/new_chronique.html', context)


@login_required(login_url='login')
def confirmChronique(request, pk):
    chronique = Chronique.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "chronique"

    context = {'page_title': page_title,
               'chronique': chronique, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def addChronique(request):
    form = ChroniqueForm()

    if request.method == "POST":
        form = ChroniqueForm(request.POST, request.FILES)
        if form.is_valid():
            chronique = form.save(commit=False)
            chronique.save()
            return redirect(f'/news/{chronique.id}')

    return redirect('/')


@login_required(login_url='login')
def deleteChronique(request, pk):
    chronique = Chronique.objects.get(id=pk)
    chronique.delete()
    return redirect('/news/')
