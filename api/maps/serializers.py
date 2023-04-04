from rest_framework import serializers
from maps.models import Map, Item


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['uuid', 'name', 'description', 'url', 'background', 'overlay']


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['uuid', 'owner', 'name', 'content', 'tag', 'points']
