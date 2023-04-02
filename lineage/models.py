from django.db import models
from utils.choices import GENDER
import uuid


class Character(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    heirs = models.ManyToManyField('self', related_name="_heirs", symmetrical=False, blank=True)
    spouse = models.ForeignKey('self', related_name="_spouse", on_delete=models.CASCADE, blank=True, null=True)
    mother = models.ForeignKey('self', related_name="_mother", on_delete=models.CASCADE, blank=True, null=True)
    father = models.ForeignKey('self', related_name="_father", on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER, default='Homme')
    birth_date = models.IntegerField(blank=True, null=True)
    death_date = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    is_living = models.BooleanField(default=True)
    is_player = models.BooleanField(default=False)
    is_native = models.BooleanField(default=False)
    vassal = models.CharField(max_length=255, blank=True, null=True)
    fiche = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-last_name']


class Family(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    head = models.ForeignKey(Character, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.head.last_name

    class Meta:
        ordering = ['-created']
