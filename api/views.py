from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from .serializers import *

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/carrieres'},
        {'GET': 'api/carrieres/id'},

        {'GET': 'api/fiches'},
        {'GET': 'api/fiches/id'},
    ]
    return Response(routes)

@api_view(['GET'])
def carrieresRoutes(request):
    carrieres = Carriere.objects.all()
    serializer = CarriereSerializer(carrieres, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def carriereRoute(request, pk):
    carriere = Carriere.objects.get(id=pk)
    serializer = CarriereSerializer(carriere, many=False)
    
    if request.method == "GET":
        return Response(serializer.data)

    elif request.method == "DELETE":
        carriere.delete()
        return Response(serializer.data)

@api_view(['GET'])
def fichesRoutes(request):
    fiches = CharacterSheet.objects.all()
    serializer = FicheSerializer(fiches, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def ficheRoute(request, pk):
    fiche = CharacterSheet.objects.get(id=pk)
    serializer = CarriereSerializer(fiche, many=False)
    
    if request.method == "GET":
        return Response(serializer.data)

    elif request.method == "DELETE":
        fiche.delete()
        return Response(serializer.data)
