from django.db import models
from django.forms import CharField
from carrieres.models import Carriere

CHOICES = (
    ('Groupe', 'Groupe'),
    ('Milice(ne)', 'Milice'),
    ('Habitant(e)', 'Peuple'),
    ('Noble', 'Noblesse'),
    ('Prêtre(sse)', 'Clergé'),
    ('Banni(e)', 'Bannis'),
)


class CharacterSheet(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(
        max_length=50, choices=CHOICES, default='Groupe', blank=False, null=True)
    rank = models.IntegerField(blank=True, null=True)
    path = models.ForeignKey(Carriere, on_delete=models.SET_NULL, null=True)
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

    created = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
