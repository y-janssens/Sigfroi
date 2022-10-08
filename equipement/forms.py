from django.forms import ModelForm
from .models import Weapon, Armor, StuffSheet


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
