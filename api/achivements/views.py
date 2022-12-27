from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from succes.models import AchievementsSheet
from .serializers import AchievementsSheetsSerializer


class AchievementsSheetsViewSet(viewsets.ModelViewSet):
    queryset = AchievementsSheet.objects.all()
    serializer_class = AchievementsSheetsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'owner_id'

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return AchievementsSheet.objects.filter(owner__id=owner_id)
