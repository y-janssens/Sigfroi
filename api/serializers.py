from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet

class CarriereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriere
        exclude = ['created']

class FicheSerializer(serializers.ModelSerializer):
    path = CarriereSerializer(many=False, read_only=True)

    class Meta:
        model = CharacterSheet
        exclude = ['created']        