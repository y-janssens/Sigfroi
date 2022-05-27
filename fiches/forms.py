from django import forms
from django.forms import ModelForm
from .models import *


class CharacterSheetForm(ModelForm):
    class Meta:
        model = CharacterSheet
        fields = '__all__'


class AliasesSheetForm(ModelForm):
    class Meta:
        model = AliasesSheet
        fields = '__all__'
