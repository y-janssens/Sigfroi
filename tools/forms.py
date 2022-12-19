from django.forms import ModelForm
from .models import ProgressBar


class ProgressBarForm(ModelForm):
    class Meta:
        model = ProgressBar
        fields = ['total', 'symbol', 'progress']
