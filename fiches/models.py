from django.db import models
from carrieres.models import Carriere
from competences.models import Skill
from utils.choices import GROUPS, GENDER, MEMBER


class CharacterSheet(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(
        max_length=50, choices=GROUPS, default='Groupe', blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    path = models.ForeignKey(
        Carriere, on_delete=models.SET_NULL, blank=True, null=True)
    skills = models.ManyToManyField(
        Skill, through='competences.SkillSheet', blank=True, editable=False)
    For = models.IntegerField(blank=True, null=True, default=8)
    End = models.IntegerField(blank=True, null=True, default=8)
    Hab = models.IntegerField(blank=True, null=True, default=8)
    Char = models.IntegerField(blank=True, null=True, default=8)
    Int = models.IntegerField(blank=True, null=True, default=8)
    Ini = models.IntegerField(blank=True, null=True, default=8)
    Att = models.IntegerField(blank=True, null=True, default=8)
    Par = models.IntegerField(blank=True, null=True, default=8)
    Tir = models.IntegerField(blank=True, null=True, default=8)
    Na = models.IntegerField(blank=True, null=True, default=1)
    Pv = models.IntegerField(blank=True, null=True, default=60)

    gender = models.CharField(
        max_length=50, choices=GENDER, default='Homme', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    member = models.CharField(
        max_length=50, choices=MEMBER, default='Non', blank=False, null=False)
    avatar = models.ImageField(upload_to=(
        'avatars'), default="avatars/default.png", blank=True, null=True)

    For1V = models.IntegerField(blank=True, null=True, default=0)
    End1V = models.IntegerField(blank=True, null=True, default=0)
    Hab1V = models.IntegerField(blank=True, null=True, default=0)
    Char1V = models.IntegerField(blank=True, null=True, default=0)
    Int1V = models.IntegerField(blank=True, null=True, default=0)
    Ini1V = models.IntegerField(blank=True, null=True, default=0)
    Att1V = models.IntegerField(blank=True, null=True, default=0)
    Par1V = models.IntegerField(blank=True, null=True, default=0)
    Tir1V = models.IntegerField(blank=True, null=True, default=0)
    Na1V = models.IntegerField(blank=True, null=True, default=0)
    Pv1V = models.IntegerField(blank=True, null=True, default=0)

    For2V = models.IntegerField(blank=True, null=True, default=0)
    End2V = models.IntegerField(blank=True, null=True, default=0)
    Hab2V = models.IntegerField(blank=True, null=True, default=0)
    Char2V = models.IntegerField(blank=True, null=True, default=0)
    Int2V = models.IntegerField(blank=True, null=True, default=0)
    Ini2V = models.IntegerField(blank=True, null=True, default=0)
    Att2V = models.IntegerField(blank=True, null=True, default=0)
    Par2V = models.IntegerField(blank=True, null=True, default=0)
    Tir2V = models.IntegerField(blank=True, null=True, default=0)
    Na2V = models.IntegerField(blank=True, null=True, default=0)
    Pv2V = models.IntegerField(blank=True, null=True, default=0)

    For3V = models.IntegerField(blank=True, null=True, default=0)
    End3V = models.IntegerField(blank=True, null=True, default=0)
    Hab3V = models.IntegerField(blank=True, null=True, default=0)
    Char3V = models.IntegerField(blank=True, null=True, default=0)
    Int3V = models.IntegerField(blank=True, null=True, default=0)
    Ini3V = models.IntegerField(blank=True, null=True, default=0)
    Att3V = models.IntegerField(blank=True, null=True, default=0)
    Par3V = models.IntegerField(blank=True, null=True, default=0)
    Tir3V = models.IntegerField(blank=True, null=True, default=0)
    Na3V = models.IntegerField(blank=True, null=True, default=0)
    Pv3V = models.IntegerField(blank=True, null=True, default=0)

    For4V = models.IntegerField(blank=True, null=True, default=0)
    End4V = models.IntegerField(blank=True, null=True, default=0)
    Hab4V = models.IntegerField(blank=True, null=True, default=0)
    Char4V = models.IntegerField(blank=True, null=True, default=0)
    Int4V = models.IntegerField(blank=True, null=True, default=0)
    Ini4V = models.IntegerField(blank=True, null=True, default=0)
    Att4V = models.IntegerField(blank=True, null=True, default=0)
    Par4V = models.IntegerField(blank=True, null=True, default=0)
    Tir4V = models.IntegerField(blank=True, null=True, default=0)
    Na4V = models.IntegerField(blank=True, null=True, default=0)
    Pv4V = models.IntegerField(blank=True, null=True, default=0)

    fiche = models.CharField(max_length=255, default="https://marbrume.forumactif.com/f8-fiches-de-personnages", blank=True, null=True)

    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Aliase(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, editable=False)

    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ['owner__name']


class AliasesSheet(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, editable=False)
    aliases = models.ManyToManyField(Aliase, blank=True, symmetrical=False)

    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ['owner__name']
