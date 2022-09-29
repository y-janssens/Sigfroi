from django.db import models
import uuid


class Snapshot(models.Model):

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.created} - {str(self.uuid)}'

    class Meta:
        ordering = ['-created']
