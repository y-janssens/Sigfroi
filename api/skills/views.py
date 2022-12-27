from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from competences.models import SkillSheet, Skill
from .serializers import SkillsSerializer, SkillSheetSerializer


class SkillSheetsViewSet(viewsets.ModelViewSet):
    queryset = SkillSheet.objects.all()
    serializer_class = SkillSheetSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = "pk"

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return SkillSheet.objects.filter(owner__id=owner_id)


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
