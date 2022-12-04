from django.db import models
from fiches.models import CharacterSheet


class Chronique(models.Model):
    resume = models.TextField(max_length=1000, blank=True, null=True)
    description = models.TextField(max_length=20000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    characters = models.IntegerField(blank=True, null=True, editable=False)
    people = models.IntegerField(blank=True, null=True, editable=False)
    clergy = models.IntegerField(blank=True, null=True, editable=False)
    militia = models.IntegerField(blank=True, null=True, editable=False)
    nobles = models.IntegerField(blank=True, null=True, editable=False)
    banished = models.IntegerField(blank=True, null=True, editable=False)
    aliases = models.IntegerField(blank=True, null=True, editable=False)
    dc = models.IntegerField(blank=True, null=True, editable=False)

    def __str__(self):
        return f"{self.created}"

    class Meta:
        ordering = ['-created']


class NewsChronicle(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    item_1 = models.TextField(blank=True, null=True)
    item_2 = models.TextField(blank=True, null=True)
    item_3 = models.TextField(blank=True, null=True)
    item_4 = models.TextField(blank=True, null=True)
    item_5 = models.TextField(blank=True, null=True)

    characters = models.IntegerField(blank=True, null=True, editable=False)
    people = models.IntegerField(blank=True, null=True, editable=False)
    clergy = models.IntegerField(blank=True, null=True, editable=False)
    militia = models.IntegerField(blank=True, null=True, editable=False)
    nobles = models.IntegerField(blank=True, null=True, editable=False)
    banished = models.IntegerField(blank=True, null=True, editable=False)
    aliases = models.IntegerField(blank=True, null=True, editable=False)
    dc = models.IntegerField(blank=True, null=True, editable=False)

    honor_member = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, null=True)
    honor_member_comment = models.TextField(blank=True, null=True)
    new_members = models.ManyToManyField(CharacterSheet, blank=True, symmetrical=False, related_name="new_members")

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created']
