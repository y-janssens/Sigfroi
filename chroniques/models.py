from django.db import models


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
