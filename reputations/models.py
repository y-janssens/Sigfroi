from django.db import models
from fiches.models import CharacterSheet

GROUPS = (
    ('Groupe', 'Groupe'),
    ('Milice(ne)', 'Milice'),
    ('Habitant(e)', 'Peuple'),
    ('Noble', 'Noblesse'),
    ('Prêtre(sse)', 'Clergé'),
    ('Banni(e)', 'Bannis'),
)

STATUS = (
    ('Statut', 'Statut'),
    ('Neutre', 'Neutre'),
    ('Positive', 'Positive'),
    ('Négative', 'Négative'),
)

class ReputationBoard(models.Model):
    owner = models.ForeignKey(CharacterSheet, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.CharField(
        max_length=50, choices=GROUPS, default='Groupe', blank=True, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS, default='Statut', blank=True, null=True)

# Create your models here.
