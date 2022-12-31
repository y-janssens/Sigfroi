from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet, AliasesSheet
from reputations.models import CommonReputation


def get_reputation_options(instance, status, option):
    flavor = instance.flavor_text

    if status == 'Excellente':
        find_status = 'exalted'
    elif status == 'Positive':
        find_status = 'positive'
    elif status == 'Neutre':
        find_status = 'neutral'
    elif status == 'Négative':
        find_status = 'negative'
    elif status == 'Recherché':
        find_status = 'wanted'

    return {'title': flavor[option][find_status]['title'], 'text': flavor[option]
            [find_status]['text'], 'status': status}


class CarriereSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()

    class Meta:
        model = Carriere
        exclude = ['created']

    def get_group(self, instance):
        if instance.group == 'Habitant(e)':
            return 'peuple'
        elif instance.group == 'Banni(e)':
            return 'banni'
        elif instance.group == 'Prêtre(sse)':
            return 'clerge'
        elif instance.group == 'Noble':
            return 'noble'
        elif instance.group == 'Milice(ne)':
            return 'milice'


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        exclude = ['created']

    def create(self, validated_data):
        validated_data['group'] = validated_data['path'].group
        return CharacterSheet.objects.create(**validated_data)


class SimpleSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterSheet
        fields = ['name', 'group', 'gender', 'fiche']


class BasicReputationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonReputation
        exclude = ['id', 'flavor_text']


class ReputationSerializer(serializers.ModelSerializer):
    globalStatus = serializers.SerializerMethodField()
    kingStatus = serializers.SerializerMethodField()
    nobilityStatus = serializers.SerializerMethodField()
    peopleStatus = serializers.SerializerMethodField()
    clergyStatus = serializers.SerializerMethodField()
    militiaStatus = serializers.SerializerMethodField()
    banishedStatus = serializers.SerializerMethodField()
    labretStatus = serializers.SerializerMethodField()
    sombreboisStatus = serializers.SerializerMethodField()
    mafiaStatus = serializers.SerializerMethodField()
    guildStatus = serializers.SerializerMethodField()

    class Meta:
        model = CommonReputation
        exclude = ['id', 'flavor_text']

    def get_globalStatus(self, instance):
        return get_reputation_options(instance, instance.globalStatus, "globalStatus")

    def get_kingStatus(self, instance):
        return get_reputation_options(instance, instance.kingStatus, "kingStatus")

    def get_nobilityStatus(self, instance):
        return get_reputation_options(instance, instance.nobilityStatus, "nobilityStatus")

    def get_peopleStatus(self, instance):
        return get_reputation_options(instance, instance.peopleStatus, "peopleStatus")

    def get_clergyStatus(self, instance):
        return get_reputation_options(instance, instance.clergyStatus, "clergyStatus")

    def get_militiaStatus(self, instance):
        return get_reputation_options(instance, instance.militiaStatus, "militiaStatus")

    def get_banishedStatus(self, instance):
        return get_reputation_options(instance, instance.banishedStatus, "banishedStatus")

    def get_labretStatus(self, instance):
        return get_reputation_options(instance, instance.labretStatus, "labretStatus")

    def get_sombreboisStatus(self, instance):
        return get_reputation_options(instance, instance.sombreboisStatus, "sombreboisStatus")

    def get_mafiaStatus(self, instance):
        return get_reputation_options(instance, instance.mafiaStatus, "mafiaStatus")

    def get_guildStatus(self, instance):
        return get_reputation_options(instance, instance.guildStatus, "guildStatus")


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        fields = ['id', 'name', 'group', 'gender', 'fiche']


class AliasesSerializer(serializers.ModelSerializer):
    owner = SimpleSheetSerializer(many=False)

    class Meta:
        model = AliasesSheet
        exclude = ['created', 'id']


class AliasesSheetsSerializer(serializers.ModelSerializer):

    owner = SimpleSheetSerializer(many=False)
    aliases = AliasesSerializer(many=True)

    class Meta:
        model = AliasesSheet
        exclude = ['created', 'id']
        depth = 1
