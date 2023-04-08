from django.db import models
import uuid


class Map(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True, unique=True)
    background = models.ImageField(upload_to=(
        'maps'), blank=True, null=True)
    overlay = models.ImageField(upload_to=(
        'maps'), blank=True, null=True)

    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Item(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        Map, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=255)
    content = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    points = models.TextField(blank=True, null=True)

    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.owner.name} - {self.uuid}"

    class Meta:
        ordering = ['-created']
