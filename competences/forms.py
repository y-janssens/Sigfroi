from django import forms
from django.forms import ModelForm
from .models import *

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class SkillSheetForm(ModelForm):
    class Meta:
        model = SkillSheet
        fields = '__all__'