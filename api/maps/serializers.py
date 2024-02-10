from rest_framework import serializers
from maps.models import Map, Item


def parseMapName(value):
    return value['name'].replace(' ', '_').lower()


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['uuid', 'name', 'description', 'url', 'background', 'overlay', 'primary']

    def create(self, validated_data):
        validated_data['url'] = parseMapName(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['url'] = parseMapName(validated_data)
        return super().update(instance, validated_data)


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['uuid', 'owner', 'name', 'content', 'points', 'color', 'redirect_uri']
