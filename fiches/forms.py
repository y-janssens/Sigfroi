from django import forms
from django.forms import ModelForm
from .models import CharacterSheet

class CharacterSheetForm(ModelForm):
    class Meta:
        model = CharacterSheet
        fields = '__all__'