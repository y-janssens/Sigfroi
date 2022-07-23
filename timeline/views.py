from django.shortcuts import render
from .models import *


def timeline(request):
    page_title = "Chronologie Générale"
    items = TimelineEvent.objects.all()
    years = items.order_by('year').values_list('year', flat=True).distinct('year')[1:]

    chrono = {}

    # for i in items:
    print(years)
    

    context = {'page_title': page_title, 'items': items, 'years': years}
    return render(request, 'timeline/timeline.html', context)