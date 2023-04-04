from rest_framework import serializers
from maps.models import Map, Item


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['uuid', 'name', 'description', 'url', 'background', 'overlay']


class ItemSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['uuid', 'owner', 'name', 'content', 'tag', 'points']

    def get_points(self, instance):
        if instance.points is None:
            return []
        return instance.points
