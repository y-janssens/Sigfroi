from django.shortcuts import render, redirect
from decorators import login_required

def reals(request):
    page_title = f"Vues Temps Réel"

    context = {'page_title': page_title}
    return render(request, 'realtime/reals.html', context)

def shield(request):
    page_title = "Blason"

    context={'page_title': page_title}
    return render(request, 'realtime/shield.html', context)