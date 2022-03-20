from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from .serializers import *


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/carrieres/'},
        {'GET': 'api/carrieres/id/'},
        {'PUT': 'api/carrieres/id/'},
        {'DELETE': 'api/carrieres/id/'},
        {'POST': 'api/carrieres/add/'},

        {'GET': 'api/fiches/'},
        {'GET': 'api/fiches/id/'},
        {'PUT': 'api/fiches/id/'},
        {'DELETE': 'api/fiches/id/'},
        {'POST': 'api/fiches/add/'},
    ]
    return Response(routes)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def createCarriere(request):
    serializer = CarriereSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def carrieresRoutes(request):
    carrieres = Carriere.objects.all()
    serializer = CarriereSerializer(carrieres, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def carriereRoute(request, pk):
    carriere = Carriere.objects.get(id=pk)

    serializer = CarriereSerializer(carriere, many=False)

    if request.method == "GET":
        return Response(serializer.data)

    elif request.method == "DELETE":
        carriere.delete()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CarriereSerializer(carriere, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def carriereNameRoute(request, pk):
    carriere = Carriere.objects.get(name=pk)
    serializer = CarriereSerializer(carriere, many=False)    
    return Response(serializer.data)


@api_view(['POST'])
def createFiche(request):
    path = Carriere.objects.get(name__iexact=request.data['path'])
    serializer = FicheSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(path=path)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def fichesRoutes(request):
    fiches = CharacterSheet.objects.all()
    serializer = FicheSerializer(fiches, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def ficheRoute(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    serializer = FicheSerializer(fiche, many=False)

    if request.method == "GET":
        return Response(serializer.data)

    elif request.method == "DELETE":
        fiche.delete()
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FicheSerializer(fiche, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
