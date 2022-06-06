from django.shortcuts import render, redirect

def battler(request):
    url = f"https://{request.META['HTTP_HOST']}/battle/iframe"
    context = {'url': url}
    return render(request, 'combat/battle.html', context)

def battlerIframe(request):
    return render(request, 'combat/battle_iframe.html')
