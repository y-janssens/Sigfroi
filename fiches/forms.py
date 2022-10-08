from django.forms import ModelForm
from .models import CharacterSheet, AliasesSheet


class CharacterSheetForm(ModelForm):
    class Meta:
        model = CharacterSheet
        fields = '__all__'


class AliasesSheetForm(ModelForm):
    class Meta:
        model = AliasesSheet
        fields = '__all__'
