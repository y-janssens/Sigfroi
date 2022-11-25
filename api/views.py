from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from reputations.models import CommonReputation
from timeline.models import TimelineEvent
from equipement.models import Armor, Weapon
from competences.models import SkillSheet, Skill
from reputations.text import flavorText
from .serializers import (CarriereSerializer, FicheSerializer, FicheSimpleListSerializer, ReputationSerializer,
                          SkillsSerializer, SkillSheetSerializer, WeaponsSerializer, ArmorsSerializer, TimelineEventSerializer)
from .filters import StandardResultsSetPagination


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'POST': 'api/token'},
        {'GET': 'api/token/refresh'},

        {'GET': 'api/flavor/'},

        {'GET': 'api/carrieres/'},
        {'GET': 'api/carrieres/id/'},
        {'PUT': 'api/carrieres/edit/id/'},
        {'DELETE': 'api/carrieres/edit/id/'},
        {'POST': 'api/carrieres/add/'},

        {'GET': 'api/fiches/'},
        {'GET': 'api/fiches/id/'},
        {'PUT': 'api/fiches/edit/id/'},
        {'DELETE': 'api/fiches/edit/id/'},
        {'POST': 'api/fiches/add/'},

        {'GET': 'api/reputations/id'},
        {'PUT': 'api/reputations/edit/id'},

        {'GET': 'api/competences/'},
        {'GET': 'api/competences/id'},

        {'GET': 'api/equipement/armes/'},
        {'GET': 'api/equipement/armes/id'},

        {'GET': 'api/equipement/armures/'},
        {'GET': 'api/equipement/armures/id'},

        {'GET': 'api/timeline/'},
        {'GET': 'api/timeline/id'},
    ]
    return Response(routes)


@api_view(['GET'])
def reputationsTextRoute(request):
    text = flavorText
    return Response(text)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCarriere(request):
    serializer = CarriereSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def carrieresRoutes(request):
    carrieres = Carriere.objects.all()
    serializer = CarriereSerializer(carrieres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def carriereRoute(request, pk):
    carriere = Carriere.objects.get(id=pk)
    serializer = CarriereSerializer(carriere, many=False)
    return Response(serializer.data)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def editCarriereRoute(request, pk):
    carriere = Carriere.objects.get(id=pk)
    serializer = CarriereSerializer(carriere, many=False)

    if request.method == "DELETE":
        carriere.delete()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CarriereSerializer(carriere, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createFiche(request):
    path = Carriere.objects.get(name__iexact=request.data['path'])
    serializer = FicheSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(path=path)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fichesRoutes(request):
    fiches = CharacterSheet.objects.all()
    serializer = FicheSerializer(fiches, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ficheRoute(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    serializer = FicheSerializer(fiche, many=False)
    return Response(serializer.data)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def editFicheRoute(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    serializer = FicheSerializer(fiche, many=False)

    if request.method == "DELETE":
        fiche.delete()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FicheSerializer(fiche, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def reputationRoute(request, pk):
    reputation = CommonReputation.objects.get(owner_id=pk)
    serializer = ReputationSerializer(reputation, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editReputationRoute(request, pk):
    reputation = CommonReputation.objects.get(owner_id=pk)
    serializer = ReputationSerializer(reputation, many=False)

    if request.method == "PUT":
        serializer = ReputationSerializer(reputation, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def competencesRoutes(request):
    competences = Skill.objects.all()
    serializer = SkillsSerializer(competences, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def competenceRoute(request, pk):
    competences = Skill.objects.get(id=pk)
    serializer = SkillsSerializer(competences, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def weaponsRoutes(request):
    weapons = Weapon.objects.all()
    serializer = WeaponsSerializer(weapons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def weaponRoute(request, pk):
    weapons = Weapon.objects.get(id=pk)
    serializer = WeaponsSerializer(weapons, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def armorsRoutes(request):
    armors = Armor.objects.all()
    serializer = ArmorsSerializer(armors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def armorRoute(request, pk):
    armors = Armor.objects.get(id=pk)
    serializer = ArmorsSerializer(armors, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def timelineRoutes(request):
    carrieres = TimelineEvent.objects.all()
    serializer = TimelineEventSerializer(carrieres, many=True)
    return Response(serializer.data)


class SheetsViewSet(viewsets.ModelViewSet):
    queryset = CharacterSheet.objects.all()
    serializer_class = FicheSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'group', 'path__name', 'gender', 'status']
    filterset_fields = ['is_active']


class SimpleSheetsViewSet(viewsets.ModelViewSet):
    queryset = CharacterSheet.objects.all()
    serializer_class = FicheSimpleListSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'group', 'path__name', 'gender', 'status']
    filterset_fields = ['is_active']


class PathViewSet(viewsets.ModelViewSet):
    queryset = Carriere.objects.all()
    serializer_class = CarriereSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'group']


class SkillSheetsViewSet(viewsets.ModelViewSet):
    queryset = SkillSheet.objects.all()
    serializer_class = SkillSheetSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer
