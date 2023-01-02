from django.shortcuts import render, redirect
from utils.decorators import login_required
from fiches.models import CharacterSheet
from .models import Skill, SkillSheet
from .forms import SkillForm, SkillSheetForm
from utils.skills import search_skills, paginate_skills
from utils.common import fill_confirmation_dict


@login_required(login_url='login')
def competences(request):
    competences = Skill.objects.all()
    form = SkillForm()
    competences, search_query = search_skills(request)
    custom_range, competences = paginate_skills(request, competences, 40)
    page_title = "Compétences"
    context = {'competences': competences, 'page_title': page_title,
               'form': form, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'competences/competences.html', context)


@login_required(login_url='login')
def competence(request, pk):
    skill = Skill.objects.get(id=pk)
    form = SkillForm(instance=skill)
    page_title = f"Compétence: {skill.name}"
    context = {'skill': skill, 'form': form, 'page_title': page_title}
    return render(request, 'competences/competence.html', context)


@login_required(login_url='login')
def addCompetence(request):
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            competence = form.save(commit=False)
            competence.save()
            return redirect('/competences')

    return redirect('/competences')


@login_required(login_url='login')
def editCompetence(request, pk):
    competence = Skill.objects.get(id=pk)
    form = SkillForm(instance=competence)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=competence)

        if form.is_valid():
            form.save()
            return redirect(f'/competences/{competence.id}')

    return redirect(f'/competences/{competence.id}')


@login_required(login_url='login')
def deleteCompetence(request, pk):
    competence = Skill.objects.get(id=pk)
    competence.delete()
    return redirect('/competences')


@login_required(login_url='login')
def confirmCompetence(request, pk):
    skill = Skill.objects.get(id=pk)
    context = fill_confirmation_dict(skill.name, "delete_competence", skill.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def addSkillSheet(request, pk):
    form = SkillSheetForm()
    fiche = CharacterSheet.objects.get(id=pk)
    if request.method == "POST":
        for i in request.POST.getlist('send-skill'):
            form = SkillSheetForm(request.POST)
            if form.is_valid():
                competence = form.save(commit=False)
                competence.owner = fiche
                competence.skill = Skill.objects.get(name=i)
                competence.save()
        return redirect(f'/fiche/{fiche.id}')

    return redirect(f'/fiche/{fiche.id}')


@login_required(login_url='login')
def editSkillSheet(request, pk):
    sheet = SkillSheet.objects.get(id=pk)
    form = SkillSheetForm(instance=sheet)

    if request.method == "POST":

        form = SkillSheetForm(request.POST, instance=sheet)
        if form.is_valid():
            form.save()
            return redirect(f'/fiche/{sheet.owner.id}')

    return redirect(f'/fiche/{sheet.owner.id}')


@login_required(login_url='login')
def confirmSkillSheet(request, pk):
    skill = SkillSheet.objects.get(id=pk)
    context = fill_confirmation_dict(skill.skill.name, "delete_skillSheet", skill.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def deleteSkillSheet(request, pk):
    skill = SkillSheet.objects.get(id=pk)
    skill.delete()
    return redirect(f'/fiche/{skill.owner.id}')


def SkillSheetIframe(request):
    competences = Skill.objects.all()
    page_title = "Compétences"
    context = {'competences': competences, 'page_title': page_title}
    return render(request, 'competences/competences_iframe.html', context)
