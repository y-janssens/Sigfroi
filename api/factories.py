import factory
from backup.models import Snapshot
from lineage.models import Character


class SnapShotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snapshot

    uuid = factory.Faker("uuid4")
    content = factory.Faker("text")


class CharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Character

    first_name = factory.Faker("text")
    last_name = factory.Faker("text")
    father = factory.SubFactory('api.factories.CharacterFactory', father=None)
