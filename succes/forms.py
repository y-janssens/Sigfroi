from django.forms import ModelForm
from .models import AchievementsSheet


class AchievementsheetForm(ModelForm):
    class Meta:
        model = AchievementsSheet
        fields = '__all__'
