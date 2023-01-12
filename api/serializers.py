from rest_framework import serializers
from timeline.models import TimelineEvent
from lineage.models import Family


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'
        depth = 1


class LineageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['uuid', 'head']
        depth = 10
