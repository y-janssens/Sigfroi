from .models import CharacterSheet
from reputations.models import *
from competences.models import *
from django.db.models.signals import post_save

skill_name = ""


def createFiche(sender, instance, created, **kwargs):
    if created:
        fiche = instance
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
