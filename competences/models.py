from django.db import models
from choices import *


class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField(max_length=2000, blank=True, null=True)
    hasLevel = models.CharField(
        max_length=50, choices=MEMBER, default='Oui', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SkillSheet(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, null=True, editable=False)
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    level = models.CharField(
        max_length=50, choices=LEVELS, default='Niveau 1', blank=True, null=True)

    def __str__(self):
        return f'{self.owner.name} - {self.skill.name} - {self.level}'

    class Meta:
        unique_together = [['owner', 'skill']]

    class Meta:
        ordering = ['skill']
