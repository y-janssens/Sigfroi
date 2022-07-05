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

def gates(request):
    page_title = "Herse"

    context={'page_title': page_title}
    return render(request, 'realtime/gates.html', context)


def walls(request):
    page_title = "Remparts"

    context={'page_title': page_title}
    return render(request, 'realtime/walls.html', context)