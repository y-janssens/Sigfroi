from rest_framework import viewsets

from .serializers import CardSheetsSerializer
from cartes.models import CardSheet


class CardSheetViewSet(viewsets.ModelViewSet):
    queryset = CardSheet.objects.all()
    serializer_class = CardSheetsSerializer
    lookup_fields = "pk"

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        print(self.kwargs)
        return CardSheet.objects.filter(owner__id=owner_id)
