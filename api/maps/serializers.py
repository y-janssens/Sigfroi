from rest_framework import serializers
from maps.models import Map, Item


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['uuid', 'name', 'description', 'url', 'background', 'overlay']

    def create(self, validated_data):
        validated_data['url'] = validated_data['name'].replace(' ', '_').lower()
        return super().create(validated_data)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['uuid', 'owner', 'name', 'content', 'points']
