from django.db.models.signals import post_save
from fiches.models import CharacterSheet
from .models import Chronique, NewsChronicle
from fiches.models import AliasesSheet


def createChronicle(sender, instance, created, **kwargs):
    aliases = AliasesSheet.objects.all()

    charactersCount = CharacterSheet.objects.all().filter(is_active=True).count()
    noblesCount = CharacterSheet.objects.filter(
        group="Noble").filter(is_active=True).count()
    militiaCount = CharacterSheet.objects.filter(
        group="Milice(ne)").filter(is_active=True).count()
    peopleCount = CharacterSheet.objects.filter(
        group="Habitant(e)").filter(is_active=True).count()
    clergyCount = CharacterSheet.objects.filter(
        group="Prêtre(sse)").filter(is_active=True).count()
    banishedCount = CharacterSheet.objects.filter(
        group="Banni(e)").filter(is_active=True).count()

    owners = []
    owned = []

    for i in aliases.all():
        if (len(i.aliases.all()) > 0):
            owners.append(i)
        for z in i.aliases.all():
            owned.append(z)

    if created:
        chronique = instance
        chronique.characters = charactersCount
        chronique.nobles = noblesCount
        chronique.militia = militiaCount
        chronique.people = peopleCount
        chronique.clergy = clergyCount
        chronique.banished = banishedCount
        chronique.aliases = len(owners)
        chronique.dc = len(owned)

        chronique.save()


post_save.connect(createChronicle, sender=Chronique)
post_save.connect(createChronicle, sender=NewsChronicle)
