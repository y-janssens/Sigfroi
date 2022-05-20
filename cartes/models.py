from django.db import models
from fiches.models import *

class Card(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to=('avatars'), blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class CardSheet(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, null=True, editable=False)
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.owner.name} - {self.card.name}'

    class Meta:
        unique_together = [['owner', 'card']]

    class Meta:
        ordering = ['owner']