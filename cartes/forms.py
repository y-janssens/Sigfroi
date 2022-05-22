from django import forms
from django.forms import ModelForm
from .models import *

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

class CardSheetForm(ModelForm):
    class Meta:
        model = CardSheet
        fields = '__all__'