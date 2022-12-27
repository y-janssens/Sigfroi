import pytest
from rest_framework import status
from api.factories import SnapShotFactory


@pytest.mark.django_db
def test_create_snapshot(client):
    response = client.post('/api/backups')

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_download_file(client):
    snap = SnapShotFactory(content="test")

    response = client.get(f'/api/backups/{snap.uuid}/download_file')

    assert response.status_code == 200
    assert response.headers['Content-Disposition'] == f'attachment; filename={snap.uuid}.json'
    assert int(response.headers['Content-Length']) == len(snap.content)
