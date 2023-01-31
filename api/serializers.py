from rest_framework import serializers
from timeline.models import TimelineEvent
from lineage.models import Family, Character


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'
        depth = 1


class SpouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        exclude = ['heirs', 'spouse', 'mother', 'father']


class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['first_name', 'last_name']


class HeirsSerializer(serializers.ModelSerializer):

    heirs = serializers.SerializerMethodField()
    spouse = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = '__all__'
        depth = 1

    def get_heirs(self, instance):
        return HeirsSerializer(instance.heirs.all(), many=True).data

    def get_spouse(self, instance):
        if not instance.spouse:
            return None
        return SpouseSerializer(instance.spouse).data


class CharacterSerializer(serializers.ModelSerializer):

    spouse = serializers.SerializerMethodField()
    mother = serializers.SerializerMethodField()
    father = serializers.SerializerMethodField()
    heirs = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = ['id', 'first_name', 'last_name', 'gender', 'father', 'mother', 'spouse',
                  'status', 'is_player', 'is_native', 'is_living', 'vassal', 'fiche', 'heirs']
        depth = 1

    def get_spouse(self, instance):
        if not instance.spouse:
            return None
        return SpouseSerializer(instance.spouse).data

    def get_mother(self, instance):
        if not instance.mother:
            return None
        return SpouseSerializer(instance.mother).data

    def get_father(self, instance):
        if not instance.father:
            return None
        return SpouseSerializer(instance.father).data

    def get_heirs(self, instance):
        return HeirsSerializer(instance.heirs.all(), many=True).data


class TreeSerializer(serializers.ModelSerializer):

    head = serializers.SerializerMethodField()

    class Meta:
        model = Family
        fields = ['uuid', 'head']
        depth = 1

    def get_head(self, instance):
        return CharacterSerializer(instance.head).data


class TreesListSerializer(serializers.ModelSerializer):

    head = serializers.SerializerMethodField()

    class Meta:
        model = Family
        fields = ['uuid', 'head']

    def get_head(self, instance):
        return HeadSerializer(instance.head).data
