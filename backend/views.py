from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import Http404  

def home(request):
    return redirect('/fiches')
  
def view_404(request, exception=None):
    return HttpResponseRedirect("/")