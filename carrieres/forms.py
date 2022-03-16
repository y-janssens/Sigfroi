from django import forms
from django.forms import ModelForm
from .models import Carriere

class CareerForm(ModelForm):
    class Meta:
        model = Carriere
        fields = '__all__'