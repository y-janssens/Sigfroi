from .models import CharacterSheet, AliasesSheet, Aliase
from reputations.models import CommonReputation
from competences.models import SkillSheet, Skill
from cartes.models import Card, CardSheet
from succes.models import AchievementsSheet
from django.db.models.signals import post_save


def createFiche(sender, instance, created, **kwargs):
    if created:
        fiche = instance
        Aliase.objects.create(owner=fiche)
        AliasesSheet.objects.create(owner=fiche)
        Card.objects.create(ref=fiche)
        CardSheet.objects.create(
            owner=fiche, card=Card.objects.get(ref=fiche))
        CommonReputation.objects.create(
            owner=fiche
        )
        AchievementsSheet.objects.create(
            owner=fiche
        )

        if fiche.group == 'Milice(ne)':
            SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Esquive'),
                level='Unique'
            )
        elif fiche.group == 'Noble':
            SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Alphabétisation'),
                level='Unique'
            )
        elif fiche.group == 'Prêtre(sse)':
            SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Doctrine du Culte')
            )
        elif fiche.group == 'Banni(e)':
            SkillSheet.objects.create(
                owner=fiche,
                skill=Skill.objects.get(name='Survie en Milieu Hostile')
            )


post_save.connect(createFiche, sender=CharacterSheet)
