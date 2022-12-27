from rest_framework import serializers
from succes.models import AchievementsSheet


class AchievementsSheetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementsSheet
        fields = '__all__'
