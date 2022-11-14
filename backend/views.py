from django.shortcuts import redirect, HttpResponseRedirect


def home(request):
    return redirect('/fiches')


def view_404(request, exception=None):
    return HttpResponseRedirect("/fiches")
