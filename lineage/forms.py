from django.forms import ModelForm
from .models import Family


class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = ['head']
