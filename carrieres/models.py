from email.policy import default
from django.db import models
from choices import RANKS


class Carriere(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)
    rank = models.IntegerField(choices=RANKS, default=1, blank=True, null=True)

    For1 = models.IntegerField(blank=True, null=True)
    End1 = models.IntegerField(blank=True, null=True)
    Hab1 = models.IntegerField(blank=True, null=True)
    Char1 = models.IntegerField(blank=True, null=True)
    Int1 = models.IntegerField(blank=True, null=True)
    Ini1 = models.IntegerField(blank=True, null=True)
    Att1 = models.IntegerField(blank=True, null=True)
    Par1 = models.IntegerField(blank=True, null=True)
    Tir1 = models.IntegerField(blank=True, null=True)
    Na1 = models.IntegerField(blank=True, null=True)
    Pv1 = models.IntegerField(blank=True, null=True)

    For2 = models.IntegerField(blank=True, null=True)
    End2 = models.IntegerField(blank=True, null=True)
    Hab2 = models.IntegerField(blank=True, null=True)
    Char2 = models.IntegerField(blank=True, null=True)
    Int2 = models.IntegerField(blank=True, null=True)
    Ini2 = models.IntegerField(blank=True, null=True)
    Att2 = models.IntegerField(blank=True, null=True)
    Par2 = models.IntegerField(blank=True, null=True)
    Tir2 = models.IntegerField(blank=True, null=True)
    Na2 = models.IntegerField(blank=True, null=True)
    Pv2 = models.IntegerField(blank=True, null=True)

    For3 = models.IntegerField(blank=True, null=True)
    End3 = models.IntegerField(blank=True, null=True)
    Hab3 = models.IntegerField(blank=True, null=True)
    Char3 = models.IntegerField(blank=True, null=True)
    Int3 = models.IntegerField(blank=True, null=True)
    Ini3 = models.IntegerField(blank=True, null=True)
    Att3 = models.IntegerField(blank=True, null=True)
    Par3 = models.IntegerField(blank=True, null=True)
    Tir3 = models.IntegerField(blank=True, null=True)
    Na3 = models.IntegerField(blank=True, null=True)
    Pv3 = models.IntegerField(blank=True, null=True)

    For4 = models.IntegerField(blank=True, null=True)
    End4 = models.IntegerField(blank=True, null=True)
    Hab4 = models.IntegerField(blank=True, null=True)
    Char4 = models.IntegerField(blank=True, null=True)
    Int4 = models.IntegerField(blank=True, null=True)
    Ini4 = models.IntegerField(blank=True, null=True)
    Att4 = models.IntegerField(blank=True, null=True)
    Par4 = models.IntegerField(blank=True, null=True)
    Tir4 = models.IntegerField(blank=True, null=True)
    Na4 = models.IntegerField(blank=True, null=True)
    Pv4 = models.IntegerField(blank=True, null=True)

    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
