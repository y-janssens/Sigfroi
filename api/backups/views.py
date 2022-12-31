from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import FileResponse
from backup.models import Snapshot
from .serializers import SnapShotSerializer
from utils.backup import backup_send_mail
import os


class BackupViewSet(viewsets.ModelViewSet):

    queryset = Snapshot.objects.all()
    serializer_class = SnapShotSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        backup_send_mail()
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=True)
    def download_file(self, request, pk):
        snapshot = Snapshot.objects.get(uuid=pk)
        filename = f'{snapshot.uuid}.json'

        with open(filename, 'w') as file:
            file.write(snapshot.content)

        file = open(filename, 'rb')
        response = FileResponse(file)

        response['Content-Disposition'] = f'attachment; filename={filename}'
        os.remove(filename)
        return response
