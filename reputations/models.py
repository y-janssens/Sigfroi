from django.db import models
from fiches.models import CharacterSheet

from choices import *


class PeopleReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    militiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    sombreboisStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    mafiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    guildStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)

    def __str__(self):
        return self.owner.name


class ClergyReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=True)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    militiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    sombreboisStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    mafiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    guildStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)

    def __str__(self):
        return self.owner.name


class MilitiaReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=True)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    militiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    sombreboisStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    mafiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    guildStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)

    def __str__(self):
        return self.owner.name


class NobilityReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=True)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    militiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    sombreboisStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    mafiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    guildStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)

    def __str__(self):
        return self.owner.name


class BanishedReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=True)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=False, null=False)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=False, null=False)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=False, null=False)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=False, null=False)
    militiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=False, null=False)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=False, null=False)
    sombreboisStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    banishedStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=False, null=False)
    mafiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)
    guildStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=False, null=False)

    def __str__(self):
        return self.owner.name
