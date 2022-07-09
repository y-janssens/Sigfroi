from django.shortcuts import render

def terminal(request):
    page_title = "Terminal"

    context = {'page_title': page_title}

    return render(request, 'terminal/index.html', context)
