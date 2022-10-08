from django.forms import ModelForm
from .models import Skill, SkillSheet


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class SkillSheetForm(ModelForm):
    class Meta:
        model = SkillSheet
        fields = '__all__'
