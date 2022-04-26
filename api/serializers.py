from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from reputations.models import CommonReputation

class CarriereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriere
        exclude = ['created']

class FicheSerializer(serializers.ModelSerializer):
    path = CarriereSerializer(many=False, read_only=True)

    class Meta:
        model = CharacterSheet
        exclude = ['created']        

class ReputationSerializer(serializers.ModelSerializer):
    owner = FicheSerializer(many=False, read_only=True)

    class Meta:
        model = CommonReputation
        fields = '__all__'
        
        depth = 1