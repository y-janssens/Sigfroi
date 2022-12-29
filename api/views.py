from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from timeline.models import TimelineEvent
from .serializers import TimelineEventSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    # Since this view points to a standlone front module, authentication is not required
    queryset = TimelineEvent.objects.all()
    serializer_class = TimelineEventSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['year']
