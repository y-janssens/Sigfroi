from django import forms
from django.forms import ModelForm
from .models import *


class ChroniqueForm(ModelForm):
    class Meta:
        model = Chronique
        fields = '__all__'