from django import forms
from django.forms import ModelForm
from .models import Chronique, NewsChronicle


class ChroniqueForm(ModelForm):
    class Meta:
        model = Chronique
        fields = '__all__'


class NewsChroniqueForm(ModelForm):

    honor_member_comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Ajouter un commentaire concernant le membre à l'honneur"}
        ),
    )

    class Meta:
        model = NewsChronicle
        fields = '__all__'
