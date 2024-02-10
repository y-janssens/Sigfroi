from django.db import models
import uuid

color_0 = '#d0021b'
color_1 = '#f5a623'
color_2 = '#f8e71c'
color_3 = '#8b572a'
color_4 = '#7ed321'
color_5 = '#417505'
color_6 = '#bd10e0'
color_7 = '#ff6900'
color_8 = '#0032fa'
color_9 = '#7bdcb5'
color_10 = '#00d084'
color_11 = '#8ed1fc'
color_12 = '#0693e3'
color_13 = '#abb8c3'
color_14 = '#eb144c'
color_15 = '#f78da7'

COLORS = [
    (color_0, "#d0021b"),
    (color_1, "#f5a623"),
    (color_2, "#f8e71c"),
    (color_3, "#8b572a"),
    (color_4, "#7ed321"),
    (color_5, "#417505"),
    (color_6, "#bd10e0"),
    (color_7, "#ff6900"),
    (color_8, "#0032fa"),
    (color_9, "#7bdcb5"),
    (color_10, "#00d084"),
    (color_11, "#8ed1fc"),
    (color_12, "#0693e3"),
    (color_13, "#abb8c3"),
    (color_14, "#eb144c"),
    (color_15, "#f78da7"),
]


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
    primary = models.BooleanField(default=False, null=False)

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
    color = models.CharField(max_length=7, choices=COLORS, default=color_0, blank=False, null=False)
    redirect_uri = models.CharField(max_length=255, default=None, null=True)
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.owner.name} - {self.uuid}"

    class Meta:
        ordering = ['-created']
