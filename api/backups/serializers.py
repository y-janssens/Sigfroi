from rest_framework import serializers
from backup.models import Snapshot


class SnapShotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snapshot
        exclude = ['content']
