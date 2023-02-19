import pytest
from lineage.models import Character
from django.test import Client
import csv
import io


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_parse_characters(client):

    csv_data = io.StringIO()

    writer = csv.writer(csv_data)
    writer.writerow(['Aliénor', 'Montfort de Brieu', '', 'Audouin II Montfort de Brieu', '', '', '', '', '', '', '', ''])
    writer.writerow(['Audouin II', 'Montfort de Brieu', '', '', '', '', '', '', '', '', '', ''])
    csv_data.seek(0)

    client.post('/lineage/characters/add', {'file_form': csv_data}, format='multipart', follow=True)

    characters = Character.objects.all().count()

    assert characters == 2
