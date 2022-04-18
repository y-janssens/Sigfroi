from django.db import models
from fiches.models import CharacterSheet

from choices import GROUPS, STATUS


class PeopleReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)

    def __str__(self):
        return self.owner.name


class ClergyReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)

    def __str__(self):
        return self.owner.name


class MilitiaReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)

    def __str__(self):
        return self.owner.name


class NobilityReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)

    def __str__(self):
        return self.owner.name


class BanishedReputation(models.Model):
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    globalStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=True, null=True)
    kingStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=True, null=True)
    nobilityStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=True, null=True)
    peopleStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=True, null=True)
    clergyStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=True, null=True)
    labretStatus = models.CharField(
        max_length=50, choices=STATUS, default='Négative', blank=True, null=True)
    banishedStatus = models.CharField(
        max_length=50, choices=STATUS, default='Positive', blank=True, null=True)
    mafiaStatus = models.CharField(
        max_length=50, choices=STATUS, default='Neutre', blank=True, null=True)

    def __str__(self):
        return self.owner.name
