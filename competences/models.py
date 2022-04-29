from django.db import models
from choices import *


class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
