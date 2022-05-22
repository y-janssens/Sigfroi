from django.db import models
from fiches.models import *

class Card(models.Model):
    ref = models.ForeignKey(CharacterSheet, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ref.name

    class Meta:
        ordering = ['ref']
                

class CardSheet(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, null=True, editable=False)
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.owner.name} - {self.card if self.card else None}'

    class Meta:
        unique_together = [['owner', 'card']]

    class Meta:
        ordering = ['owner']