from rest_framework import serializers
from equipement.models import Weapon, Armor, StuffSheet
from fiches.models import CharacterSheet


class WeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class ArmorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = '__all__'


class StuffSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuffSheet
        fields = ['id', 'owner', 'armor', 'weapon']

    def create(self, validated_data):

        owner_id = self.context['request'].data['owner']
        weapon_id = self.context['request'].data.get('weapon', None)
        armor_id = self.context['request'].data.get('armor', None)

        if weapon_id is not None:
            validated_data['weapon'] = Weapon.objects.get(id=weapon_id)

        if armor_id is not None:
            validated_data['armor'] = Armor.objects.get(id=armor_id)

        validated_data['owner'] = CharacterSheet.objects.get(id=owner_id)
        return StuffSheet.objects.create(**validated_data)
