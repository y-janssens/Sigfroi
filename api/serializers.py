from rest_framework import serializers
from timeline.models import TimelineEvent


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'
        depth = 1
