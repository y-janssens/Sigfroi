import factory
from backup.models import Snapshot


class SnapShotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snapshot

    uuid = factory.Faker("uuid4")
    content = factory.Faker("text")
