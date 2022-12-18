from django.forms import ModelForm
from .models import Pantheon


class PantheonForm(ModelForm):
    class Meta:
        model = Pantheon
        fields = ['name', 'group', 'inscription_date', 'completion_date', 'fiche']
