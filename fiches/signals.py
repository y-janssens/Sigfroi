from .models import CharacterSheet
from reputations.models import *
from django.db.models.signals import post_save


def createFiche(sender, instance, created, **kwargs):
    if created:
        fiche = instance
        if fiche.group == 'Habitant(e)':
            reputation = PeopleReputation.objects.create(
                owner=fiche
            )
        elif fiche.group == 'Milice(ne)':
            reputation = MilitiaReputation.objects.create(
                owner=fiche
            )
        elif fiche.group == 'Noble':
            reputation = NobilityReputation.objects.create(
                owner=fiche
            )
        elif fiche.group == 'Prêtre(sse)':
            reputation = ClergyReputation.objects.create(
                owner=fiche
            )
        elif fiche.group == 'Banni(e)':
            reputation = BanishedReputation.objects.create(
                owner=fiche
            )


post_save.connect(createFiche, sender=CharacterSheet)
