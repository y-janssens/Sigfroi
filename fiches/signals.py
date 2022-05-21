from .models import *
from reputations.models import *
from competences.models import *
from cartes.models import *
from django.db.models.signals import post_save


def createFiche(sender, instance, created, **kwargs):
    if created:
        fiche = instance
        alias = Aliase.objects.create(owner=fiche)
        aliasesSheet = AliasesSheet.objects.create(owner=fiche)
        card = Card.objects.create(ref=fiche)
        cardSheet = CardSheet.objects.create(owner=fiche, card = Card.objects.get(ref=fiche))
        reputations = CommonReputation.objects.create(
            owner=fiche
        )

        if fiche.group == 'Milice(ne)':
            competence = SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Esquive'),
                level='Unique'
            )
        elif fiche.group == 'Noble':
            competence = SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Alphabétisation'),
                level='Unique'
            )
        elif fiche.group == 'Prêtre(sse)':
            competence = SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Doctrine du Culte')
            )
        elif fiche.group == 'Banni(e)':
            competence = SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Survie en Milieu Hostile')
            )


post_save.connect(createFiche, sender=CharacterSheet)
