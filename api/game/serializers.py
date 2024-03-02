from rest_framework import serializers
from game.models import Post, Version



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'