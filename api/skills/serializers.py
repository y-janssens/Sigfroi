from rest_framework import serializers
from fiches.models import CharacterSheet
from competences.models import Skill, SkillSheet


class SkillSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillSheet
        fields = '__all__'

    def create(self, validated_data):

        owner_id = self.context['request'].data['owner']
        skill_name = self.context['request'].data['skill']

        validated_data['skill'] = Skill.objects.get(name=skill_name)
        validated_data['level'] = 'Unique' if skill_name == 'Esquive' or skill_name == 'Alphabétisation' or skill_name == 'Ambidextrie' else 'Niveau 1'
        validated_data['owner'] = CharacterSheet.objects.get(id=owner_id)

        return SkillSheet.objects.create(**validated_data)


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
