from rest_framework import serializers
from cartes.models import Card, CardSheet
from fiches.models import CharacterSheet


class CardSheetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardSheet
        exclude = ['owner']
        depth = 1

    def create(self, validated_data):

        card_id = self.context['request'].data['card']['ref']
        owner_id = self.context['request'].data['owner']

        validated_data['card'] = Card.objects.get(id=card_id)
        validated_data['owner'] = CharacterSheet.objects.get(id=owner_id)

        return CardSheet.objects.create(**validated_data)
