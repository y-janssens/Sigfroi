from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import get_listing, get_aliases
from carrieres.models import Carriere
from fiches.models import CharacterSheet
from timeline.models import TimelineEvent
from reputations.models import CommonReputation
from .serializers import CarriereSerializer, SheetSerializer, TimelineEventSerializer, \
    ReputationSerializer, BasicReputationSerializer, ListingSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    # Since this view points to a standlone front module, authentication is not required
    queryset = TimelineEvent.objects.all()
    serializer_class = TimelineEventSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['year']


# Character sheets and related viewsets
class SheetsViewSet(viewsets.ModelViewSet):
    queryset = CharacterSheet.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SheetSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'group', 'path__name', 'gender', 'status']
    filterset_fields = ['is_active']

    @action(methods=['get'], detail=False)
    def listing(self, request):

        latest = CharacterSheet.objects.latest('created').created

        people = get_listing("Habitant(e)")
        nobles = get_listing("Noble")
        militia = get_listing("Milice(ne)")
        clergy = get_listing("Prêtre(sse)")
        banished = get_listing("Banni(e)")
        aliases = get_aliases()

        listing = {
            "latest": latest,
            "active_players": {
                "people": people,
                "nobles": nobles,
                "militia": militia,
                "clergy": clergy,
                "banished": banished
            },
            "aliases": aliases
        }

        return Response(listing)


class PathViewSet(viewsets.ModelViewSet):
    queryset = Carriere.objects.all()
    serializer_class = CarriereSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'group']


class ReputationViewSet(viewsets.ModelViewSet):
    queryset = CommonReputation.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'owner_id'

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return CommonReputation.objects.filter(owner__id=owner_id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReputationSerializer
        return BasicReputationSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = CharacterSheet.objects.all()
    serializer_class = ListingSerializer
