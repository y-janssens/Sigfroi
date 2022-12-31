from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import ProgressBar
from .forms import ProgressBarForm
from utils.common import bars_to_js


@login_required(login_url='login')
def progress_bars(request):
    bars = ProgressBar.objects.all()
    form = ProgressBarForm(instance=ProgressBar())
    bar_list = bars_to_js(ProgressBar, "uuid", "name", "color", "progress", "total", "symbol")
    page_title = "Barres de progression"
    url = "https://www.marbrume.com/tools/bars/iframe"
    context = {'bars': bars, 'page_title': page_title, "bar_list": bar_list, 'form': form, 'url': url}
    return render(request, 'tools/bars/bars.html', context)


def progress_bar_iframe(request, pk):
    bar = ProgressBar.objects.get(id=pk)
    bar_list = bars_to_js(ProgressBar, "uuid", "name", "color", "progress", "total", "symbol")
    page_title = f"Barre de progression N°{bar.id}"
    context = {'bar': bar, 'page_title': page_title, 'bar_list': bar_list}
    return render(request, 'tools/bars/bar_iframe.html', context)


@login_required(login_url='login')
def add_progress_bar(request):
    total_bars = ProgressBar.objects.all().count()

    bar = ProgressBar.objects.create(name=f"Barre N°{total_bars + 1}")
    bar.save()
    return redirect('/tools/bars/')


def edit_progress_bar(request, pk):
    bar = ProgressBar.objects.get(id=pk)

    if request.method == "POST":

        form = ProgressBarForm(request.POST, request.FILES, instance=bar)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    return redirect('/tools/bars/')


@login_required(login_url='login')
def confirm_progress_bar(request, pk):
    bar = ProgressBar.objects.get(id=pk)
    page_title = "Confirmation"
    sender = "progress bar"

    context = {'page_title': page_title, 'bar': bar, 'sender': sender}
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def delete_progress_bar(request, pk):
    bar = ProgressBar.objects.get(id=pk)
    bar.delete()
    return redirect('/tools/bars/')
