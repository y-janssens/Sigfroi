from django.db import models


class Chronique(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    resume = models.TextField(max_length=1000, blank=True, null=True)
    description = models.TextField(max_length=20000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.created} - {str(self.title)}'

    class Meta:
        ordering = ['-created']
