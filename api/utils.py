from fiches.models import CharacterSheet, AliasesSheet
from .serializers import SimpleSheetSerializer, AliasesSheetsSerializer
from django.db.models import Q


def get_listing(filter):
    query = CharacterSheet.objects.filter(Q(group=filter) & Q(is_active=True))
    males_count = CharacterSheet.objects.filter(Q(group=filter) & Q(is_active=True) & Q(gender="Homme"))
    females_count = CharacterSheet.objects.filter(Q(group=filter) & Q(is_active=True) & Q(gender="Femme"))
    serializer = SimpleSheetSerializer(query, many=True)
    return {
        "count": {"total": len(serializer.data), "males": len(males_count), "females": len(females_count)},
        "characters": serializer.data
    }


def get_aliases():
    aliases = AliasesSheet.objects.filter(Q(owner__is_active=True) & Q(aliases__isnull=False)).distinct()
    serializer = AliasesSheetsSerializer(aliases, many=True)
    owners = []
    owned = []
    ownedMales = []
    ownedFemales = []

    for i in aliases:
        if (len(i.aliases.all()) >= 1):
            owners.append(i)
        for z in i.aliases.all():
            if (z.owner.gender == "Homme"):
                ownedMales.append(z)
            else:
                ownedFemales.append(z)
            owned.append(z)

    return {
        "count": {"players": len(owners), "aliases": len(owned), "males": len(ownedMales), "females": len(ownedFemales)},
        "aliases": serializer.data
    }
