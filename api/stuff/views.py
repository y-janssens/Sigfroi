from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters

from equipement.models import StuffSheet
from .serializers import StuffSheetSerializer, ArmorsSerializer, WeaponsSerializer
from equipement.models import Armor, Weapon


class ArmorsViewSet(viewsets.ModelViewSet):
    queryset = Armor.objects.all()
    serializer_class = ArmorsSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'type']


class WeaponsViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponsSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'type']


class StuffSheetViewSet(viewsets.ModelViewSet):
    queryset = StuffSheet.objects.all()
    serializer_class = StuffSheetSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = "pk"

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        print(self.kwargs)
        return StuffSheet.objects.filter(owner__id=owner_id)
