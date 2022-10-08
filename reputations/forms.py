from django.forms import ModelForm
from .models import CommonReputation


class CommonReputationForm(ModelForm):
    class Meta:
        model = CommonReputation
        fields = '__all__'
