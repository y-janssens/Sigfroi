from django.shortcuts import render, redirect
from decorators import login_required
from .models import Skill, SkillSheet
from .forms import SkillForm
from .utils import searchSkill, paginateSkill


@login_required(login_url='login')
def competences(request):
    competences = Skill.objects.all()
    form = SkillForm()
    competences, search_query = searchSkill(request)
    custom_range, competences = paginateSkill(request, competences, 40)
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


def competencesDetails(request):
    competences = Skill.objects.all()
    context = {'competences': competences}
    return render(request, 'competences/iframe.html', context)


@login_required(login_url='login')
def deleteCompetence(request, pk):
    competence = Skill.objects.get(id=pk)
    competence.delete()
    return redirect('/competences')


@login_required(login_url='login')
def confirmCompetence(request, pk):
    competence = Skill.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "competence"

    context = {'page_title': page_title,
               'competence': competence, 'sender': sender}
    return render(request, 'base/confirm.html', context)
