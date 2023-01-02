from django.forms import ModelForm
from .models import Weapon, Armor, StuffSheet, CustomSheet


class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'


class ArmorForm(ModelForm):
    class Meta:
        model = Armor
        fields = '__all__'


class StuffSheetForm(ModelForm):
    class Meta:
        model = StuffSheet
        fields = '__all__'


class CustomSheetForm(ModelForm):
    class Meta:
        model = CustomSheet
        fields = '__all__'
