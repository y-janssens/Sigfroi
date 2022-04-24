from .models import CharacterSheet
from reputations.models import *
from django.db.models.signals import post_save


def createFiche(sender, instance, created, **kwargs):
    if created:
        fiche = instance
        reputation = CommonReputation.objects.create(
            owner=fiche
        )


post_save.connect(createFiche, sender=CharacterSheet)
