from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from maps.models import Map, Item
from .serializers import MapSerializer, ItemSerializer


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    permission_classes = [IsAuthenticated]

    serializer_class = MapSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    @action(methods=['get'], detail=True)
    def items(self, request, pk):

        queryset = Item.objects.filter(owner_id=pk)

        serializer = ItemSerializer(queryset, many=True)

        return Response(serializer.data)


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer


class PublicMapViewSet(MapViewSet):
    lookup_field = 'url'
    http_method_names = ['get']
    permission_classes = []
