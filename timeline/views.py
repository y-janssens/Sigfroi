from django.shortcuts import render

url = "https://www.marbrume.com/timeline/iframe"
page_title = "Chronologie Générale"


def timeline(request):
    context = {'page_title': page_title, 'url': url}
    return render(request, 'timeline/timeline.html', context)


def timeline_iframe(request):
    context = {'page_title': page_title, 'url': url}
    return render(request, 'timeline/timeline_iframe.html', context)
