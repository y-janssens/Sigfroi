from django import forms
from django.forms import ModelForm
from pkg_resources import require
from .models import *


class CommonReputationForm(ModelForm):
    class Meta:
        model = CommonReputation
        fields = '__all__'