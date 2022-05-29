from django.db import models
from fiches.models import *
from choices import *
from .text import *

class AchievementsSheet(models.Model):
    owner = models.ForeignKey(CharacterSheet, on_delete=models.CASCADE, blank=True, editable=False)

    for i in achievementsList:
        locals()[i['title']] = models.BooleanField(default=False, blank=False, null=False)


    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ['owner']