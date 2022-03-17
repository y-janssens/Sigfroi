from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet

class CarriereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriere
        #fields = '__all__'
        exclude = ['created']

class FicheSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        exclude = ['created']
        depth = 1