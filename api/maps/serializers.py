from rest_framework import serializers
from maps.models import Map, Item
from django.conf import settings


def parseMapName(value):
    return value['name'].replace(' ', '_').lower()


class MapSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()

    def get_filename(self, instance):
        if not settings.DEBUG:
            return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{instance.background}"
        return instance.background

    class Meta:
        model = Map
        fields = ['uuid', 'name', 'description', 'url', 'background', 'overlay', 'primary', 'filename']

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
