from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from reputations.models import CommonReputation
from competences.models import Skill, SkillSheet


class CarriereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriere
        exclude = ['created']


class SkillSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSheet
        fields = '__all__'


class FicheSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        exclude = ['created']

        depth = 1


class ReputationSerializer(serializers.ModelSerializer):
    owner = FicheSerializer(many=False, read_only=True)

    class Meta:
        model = CommonReputation
        fields = '__all__'

        depth = 1


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
