from django.forms import ModelForm
from .models import Chronique


class ChroniqueForm(ModelForm):
    class Meta:
        model = Chronique
        fields = '__all__'
