from rest_framework import serializers
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from reputations.models import CommonReputation
from competences.models import Skill, SkillSheet
from equipement.models import Weapon, Armor, StuffSheet
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


class SkillSheetSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='skill.name')
    owner = serializers.CharField(source='owner.id')
    level = serializers.SerializerMethodField()

    class Meta:
        model = SkillSheet
        fields = '__all__'

    def get_level(self, instance):
        if instance.level == 'Niveau 1':
            return 1
        elif instance.level == 'Niveau 2':
            return 2
        elif instance.level == 'Niveau 3':
            return 3
        else:
            return None

    def create(self, validated_data):

        skill_name = validated_data['skill']['name']
        owner_id = validated_data['owner']['id']

        validated_data['owner'] = CharacterSheet.objects.get(id=owner_id)
        validated_data['skill'] = Skill.objects.get(name=skill_name)
        validated_data['level'] = 'Unique' if skill_name == 'Esquive' or skill_name == 'Alphabétisation' or skill_name == 'Ambidextrie' else 'Niveau 1'
        skillSheet = SkillSheet.objects.create(**validated_data)
        return skillSheet


class StuffSheetSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = StuffSheet
        fields = ('name', 'type', 'category')

    def get_name(self, instance):
        if instance.weapon:
            return instance.weapon.name
        else:
            return instance.armor.name

    def get_type(self, instance):
        if instance.weapon:
            return instance.weapon.type
        else:
            return instance.armor.type

    def get_category(self, instance):
        if instance.weapon:
            return 'weapon'
        else:
            return 'armor'


class FicheSimpleListSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    path = serializers.SerializerMethodField()

    class Meta:
        model = CharacterSheet
        fields = ('id', 'name', 'group', 'path', 'is_active')

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

    def get_path(self, instance):
        return instance.path.name


class FicheSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    skills = serializers.SerializerMethodField()
    stuff = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    table = serializers.SerializerMethodField()
    reputations = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = CharacterSheet
        fields = ('id', 'name', 'group', 'gender', 'status', 'stats', 'table', 'skills', 'stuff', 'reputations', 'is_active')
        depth = 1

    def get_id(self, instance):
        return instance.id

    def get_gender(self, instance):
        if instance.gender == 'Homme':
            return 'male'
        else:
            return 'female'

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

    def get_skills(self, instance):
        skills = SkillSheet.objects.filter(owner_id=instance.id)
        return SkillSheetSerializer(skills, many=True).data

    def get_stuff(self, instance):
        skills = StuffSheet.objects.filter(owner_id=instance.id)
        return StuffSheetSerializer(skills, many=True).data

    def get_table(self, instance):
        path = Carriere.objects.get(name=instance.path.name)
        return CarriereSerializer(path, many=False).data

    def get_stats(self, instance):
        return {'For': instance.For, 'End': instance.End, 'Hab': instance.Hab, 'Char': instance.Char, 'Int': instance.Int,
                'Ini': instance.Ini, 'Att': instance.Att, 'Par': instance.Par, 'Tir': instance.Tir, 'Na': instance.Na, 'Pv': instance.Pv}

    def get_reputations(self, instance):
        reputations = CommonReputation.objects.get(owner_id=instance.id)
        return ReputationSerializer(reputations, many=False).data


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
        exclude = ['owner', 'id']
        depth = 1

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


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class WeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class ArmorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = '__all__'


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'

        depth = 1
