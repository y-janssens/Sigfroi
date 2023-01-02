from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import Chronique, NewsChronicle
from fiches.models import CharacterSheet
from .forms import ChroniqueForm, NewsChroniqueForm
from utils.common import chars_to_js, date_range, fill_confirmation_dict
import datetime


@login_required(login_url='login')
def chroniques(request):
    page_title = "Chroniques"
    chroniques = Chronique.objects.all()
    url = "https://www.marbrume.com/chronicles/"
    context = {"page_title": page_title, "chroniques": chroniques, "url": url}
    return render(request, 'chroniques/partners/chroniques.html', context)


def chronique(request, pk):
    chronique = Chronique.objects.get(id=pk)
    page_title = f"Chronique N°{chronique.id}"
    context = {"page_title": page_title, "chronique": chronique}
    return render(request, 'chroniques/partners/chronique.html', context)


@login_required(login_url='login')
def newChronique(request):
    form = ChroniqueForm()
    page_title = "Nouvelle Chronique"
    context = {"page_title": page_title, "form": form}
    return render(request, 'chroniques/partners/new_chronique.html', context)


@login_required(login_url='login')
def confirmChronique(request, pk):
    chronique = Chronique.objects.get(id=pk)
    date = datetime.datetime.strptime(str(chronique.created), '%Y-%m-%d %H:%M:%S.%f%z')
    month_name = date.strftime("%B")
    context = fill_confirmation_dict(f"Chronique de {month_name} {date.year}", "delete_chronique", chronique.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def addChronique(request):
    form = ChroniqueForm()

    if request.method == "POST":
        form = ChroniqueForm(request.POST, request.FILES)
        if form.is_valid():
            chronique = form.save(commit=False)
            chronique.save()
            return redirect(f'{chronique.id}/')

    return redirect('')


@login_required(login_url='login')
def deleteChronique(request, pk):
    chronique = Chronique.objects.get(id=pk)
    chronique.delete()
    return redirect('/chronicles/')


@login_required(login_url='login')
def news_chroniques(request):
    page_title = "Chroniques Mensuelles"
    chroniques = NewsChronicle.objects.all()
    url = "https://www.marbrume.com/chronicles/monthly/"
    context = {"page_title": page_title, "chroniques": chroniques, "url": url}
    return render(request, 'chroniques/monthly/news_chroniques.html', context)


@login_required(login_url='login')
def addNewsChronique(request):
    form = NewsChroniqueForm()
    if request.method == "POST":
        form = NewsChroniqueForm(request.POST)
        if form.is_valid():
            chronique = form.save(commit=False)
            new_members = CharacterSheet.objects.filter(created__range=(date_range()))
            chronique.save()
            for item in new_members:
                chronique.new_members.add(item)

            return redirect(f'{chronique.id}/')

    return redirect('monthly/new')


@login_required(login_url='login')
def edit_news_chronique(request, pk):
    chronique = NewsChronicle.objects.get(id=pk)

    if request.method == "POST":

        form = NewsChroniqueForm(request.POST, request.FILES, instance=chronique)
        if form.is_valid():
            form.save()
            return redirect(f'/chronicles/monthly/{chronique.id}')

    return redirect(f'/chronicles/monthly/{chronique.id}')


@login_required(login_url='login')
def confirm_News_Chronique(request, pk):
    chronique = NewsChronicle.objects.get(id=pk)
    context = fill_confirmation_dict(chronique.title, "delete_news_chronique", chronique.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteNewsChronique(request, pk):
    chronique = NewsChronicle.objects.get(id=pk)
    chronique.delete()
    return redirect('/chronicles/monthly')


@login_required(login_url='login')
def news_chronique(request, pk):
    form = NewsChroniqueForm()
    chronique = NewsChronicle.objects.get(id=pk)
    char_list = CharacterSheet.objects.filter(is_active=True).order_by('name')
    characters = chars_to_js(CharacterSheet, "id", "name", "avatar")
    new_members = chronique.new_members.all().order_by("name")
    page_title = chronique.title
    context = {"page_title": page_title, "chronique": chronique, "new_members": new_members, 'form': form, 'char_list': char_list, 'characters': characters}
    return render(request, 'chroniques/monthly/news_chronique.html', context)


def news_chronique_iframe(request, pk):
    chronique = NewsChronicle.objects.get(id=pk)
    new_members = chronique.new_members.all().order_by("name")
    page_title = chronique.title
    context = {"page_title": page_title, "chronique": chronique, "new_members": new_members}
    return render(request, 'chroniques/monthly/news_chronique_iframe.html', context)


@login_required(login_url='login')
def newNewsChronique(request):
    form = NewsChroniqueForm()
    char_list = CharacterSheet.objects.filter(is_active=True).order_by('name')
    characters = chars_to_js(CharacterSheet, "id", "name", "avatar")
    page_title = "Nouvelle Chronique Mensuelle"
    context = {"page_title": page_title, "form": form, 'characters': characters, 'char_list': char_list}
    return render(request, 'chroniques/monthly/new_news_chronique.html', context)
