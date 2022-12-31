from django.db import models
from utils.choices import GROUPS


class Pantheon(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    group = models.CharField(max_length=100, choices=GROUPS, default='Groupe', blank=True, null=True)
    inscription_date = models.DateField(auto_now=False)
    completion_date = models.DateField(auto_now=False)
    fiche = models.CharField(max_length=1000, default="https://marbrume.forumactif.com")
    created = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class PantheonCustom(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    group = models.CharField(max_length=100, choices=GROUPS, default='Groupe', blank=True, null=True)
    inscription_date = models.DateField(auto_now=False)
    completion_date = models.DateField(auto_now=False)
    fiche = models.CharField(max_length=1000, default="https://marbrume.forumactif.com")
    created = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
