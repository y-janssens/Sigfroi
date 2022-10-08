from django.shortcuts import redirect
from decorators import login_required
from .models import AchievementsSheet
from .forms import AchievementsheetForm
from fiches.models import CharacterSheet


@login_required(login_url='login')
def Editsuccess(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    achievements = AchievementsSheet.objects.get(owner_id=pk)
    if request.method == "POST":
        form = AchievementsheetForm(request.POST, instance=achievements)
        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')
