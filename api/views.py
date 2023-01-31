from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.db.models import Prefetch


from timeline.models import TimelineEvent
from .serializers import TimelineEventSerializer, TreeSerializer, TreesListSerializer
from lineage.models import Character, Family


class TimelineViewSet(viewsets.ModelViewSet):
    # Since this view points to a standlone front module, authentication is not required
    # But requests are restricted to GET method
    http_method_names = ['get']
    queryset = TimelineEvent.objects.all()
    serializer_class = TimelineEventSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['year']


class LineageViewSet(viewsets.ModelViewSet):
    # Since this view points to a standlone front module, authentication is not required
    # But requests are restricted to GET method
    http_method_names = ['get']
    queryset = Family.objects.all().prefetch_related(
        Prefetch('head__heirs', queryset=Character.objects.all()))

    def get_serializer_class(self):
        if self.action == 'list':
            return TreesListSerializer
        else:
            return TreeSerializer
