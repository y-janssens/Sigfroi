from django.forms import ModelForm
from .models import Pantheon, PantheonCustom


class PantheonForm(ModelForm):
    class Meta:
        model = Pantheon
        fields = ['name', 'group', 'inscription_date', 'completion_date', 'fiche']


class PantheonCustomForm(ModelForm):
    class Meta:
        model = PantheonCustom
        fields = ['name', 'group', 'inscription_date', 'completion_date', 'fiche']
