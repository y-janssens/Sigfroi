from django.db import models
from django.forms import CharField

CHOICES = (
    ('Groupe', 'Groupe'),
    ('Milice', 'Milicien(ne)'),
    ('Peuple', 'Habitant(e)'),
    ('Noblesse', 'Noble'),
    ('Clergé', 'Prêtre(sse)'),
    ('Banni', 'Banni(e)'),
)


class CharacterSheet(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(
        max_length=50, choices=CHOICES, default='Groupe', blank=False, null=True)
    rank = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=50, blank=True, null=True)
    For = models.IntegerField(blank=True, null=True, default=8)
    End = models.IntegerField(blank=True, null=True, default=8)
    Hab = models.IntegerField(blank=True, null=True, default=8)
    Char = models.IntegerField(blank=True, null=True, default=8)
    Int = models.IntegerField(blank=True, null=True, default=8)
    Ini = models.IntegerField(blank=True, null=True, default=8)
    Att = models.IntegerField(blank=True, null=True, default=8)
    Par = models.IntegerField(blank=True, null=True, default=8)
    Tir = models.IntegerField(blank=True, null=True, default=8)
    Na = models.IntegerField(blank=True, null=True, default=2)
    Pv = models.IntegerField(blank=True, null=True, default=60)
    created = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
