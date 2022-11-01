from django.shortcuts import redirect, render
from decorators import login_required
from .models import AchievementsSheet, Achievement
from .forms import AchievementsheetForm, AchievementForm
from fiches.models import CharacterSheet
from .utils import paginateAchievement, searchAchievement


@login_required(login_url='login')
def achievements(request):
    page_title = "Succès"
    succes, search_query = searchAchievement(request)
    custom_range, succes = paginateAchievement(request, succes, 18)
    
    context = {'page_title': page_title, 'succes': succes, 'search_query': search_query, 'custom_range': custom_range}

    return render(request, 'succes/achievements.html', context)

@login_required(login_url='login')
def achievement(request, pk):
    achievement = Achievement.objects.get(id=pk)
    form = AchievementForm(instance=achievement)
    page_title = f"{achievement.title}"

    context = {'page_title': page_title, 'achievement': achievement, 'form': form}

    return render(request, 'succes/achievement.html', context)

@login_required(login_url='login')
def editAchievement(request, pk):
    achievement = Achievement.objects.get(id=pk)
    
    if request.method == "POST":
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect(f'/succes/{achievement.id}')

    return redirect(f'/succes/{achievement.id}')


@login_required(login_url='login')
def editPlayerAchievement(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    achievements = AchievementsSheet.objects.get(owner_id=pk)
    if request.method == "POST":
        form = AchievementsheetForm(request.POST, instance=achievements)
        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')
