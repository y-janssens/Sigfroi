from django.db import models
from django.forms import CharField

CHOICES = (
('Milice', 'Milicien'),
('Peuple', 'Peuple'),
('Noblesse', 'Noble'),
('Clergé', 'Prêtre(sse)'),
('Banni', 'Banni'),
    )

class CharacterSheet(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    group = models.CharField(max_length=50, choices=CHOICES, blank=False, null=False)
    rank = models.IntegerField(blank=False, null=False)
    path = models.CharField(max_length=50, blank=False, null=False)
    For = models.IntegerField(blank=False, null=False, default=8)
    End = models.IntegerField(blank=False, null=False, default=8)
    Hab = models.IntegerField(blank=False, null=False, default=8)
    Char = models.IntegerField(blank=False, null=False, default=8)
    Int = models.IntegerField(blank=False, null=False, default=8)
    Ini = models.IntegerField(blank=False, null=False, default=8)
    Att = models.IntegerField(blank=False, null=False, default=8)
    Par = models.IntegerField(blank=False, null=False, default=8)
    Tir = models.IntegerField(blank=False, null=False, default=8)
    Na = models.IntegerField(blank=False, null=False, default=2)
    Pv = models.IntegerField(blank=False, null=False, default=60)
    created = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']
