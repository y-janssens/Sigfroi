from django.forms import ModelForm
from .models import AchievementsSheet, Achievement


class AchievementsheetForm(ModelForm):
    class Meta:
        model = AchievementsSheet
        fields = '__all__'


class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'text']
