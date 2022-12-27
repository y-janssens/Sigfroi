from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet, AliasesSheet
from reputations.models import CommonReputation
from timeline.models import TimelineEvent
from reputations.text import flavorText as flavor


def find_status(status):
    if status == 'Excellente':
        status = 'exalted'
    elif status == 'Positive':
        status = 'positive'
    elif status == 'Neutre':
        status = 'neutral'
    elif status == 'Négative':
        status = 'negative'
    elif status == 'Recherché':
        status = 'wanted'
    return status


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
        exclude = ['id']


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
        exclude = ['id']

    def get_globalStatus(self, instance):
        status = find_status(instance.globalStatus)

        return {'title': flavor['globalStatus'][status]['title'], 'text': flavor['globalStatus']
                [status]['text'], 'status': instance.globalStatus}

    def get_kingStatus(self, instance):
        status = find_status(instance.kingStatus)

        return {'title': flavor['kingStatus'][status]['title'], 'text': flavor['kingStatus']
                [status]['text'], 'status': instance.kingStatus}

    def get_nobilityStatus(self, instance):
        status = find_status(instance.nobilityStatus)

        return {'title': flavor['nobilityStatus'][status]['title'], 'text': flavor['nobilityStatus']
                [status]['text'], 'status': instance.nobilityStatus}

    def get_peopleStatus(self, instance):
        status = find_status(instance.peopleStatus)

        return {'title': flavor['peopleStatus'][status]['title'], 'text': flavor['peopleStatus']
                [status]['text'], 'status': instance.peopleStatus}

    def get_clergyStatus(self, instance):
        status = find_status(instance.clergyStatus)

        return {'title': flavor['clergyStatus'][status]['title'], 'text': flavor['clergyStatus']
                [status]['text'], 'status': instance.clergyStatus}

    def get_militiaStatus(self, instance):
        status = find_status(instance.militiaStatus)

        return {'title': flavor['militiaStatus'][status]['title'], 'text': flavor['militiaStatus']
                [status]['text'], 'status': instance.militiaStatus}

    def get_banishedStatus(self, instance):
        status = find_status(instance.banishedStatus)

        return {'title': flavor['banishedStatus'][status]['title'], 'text': flavor['banishedStatus']
                [status]['text'], 'status': instance.banishedStatus}

    def get_labretStatus(self, instance):
        status = find_status(instance.labretStatus)

        return {'title': flavor['labretStatus'][status]['title'], 'text': flavor['labretStatus']
                [status]['text'], 'status': instance.labretStatus}

    def get_sombreboisStatus(self, instance):
        status = find_status(instance.sombreboisStatus)

        return {'title': flavor['sombreboisStatus'][status]['title'], 'text': flavor['sombreboisStatus']
                [status]['text'], 'status': instance.sombreboisStatus}

    def get_mafiaStatus(self, instance):
        status = find_status(instance.mafiaStatus)

        return {'title': flavor['mafiaStatus'][status]['title'], 'text': flavor['mafiaStatus']
                [status]['text'], 'status': instance.mafiaStatus}

    def get_guildStatus(self, instance):
        status = find_status(instance.guildStatus)

        return {'title': flavor['guildStatus'][status]['title'], 'text': flavor['guildStatus']
                [status]['text'], 'status': instance.guildStatus}


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'
        depth = 1


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        fields = ['id', 'name', 'group', 'gender', 'fiche', 'created']


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
