from django.db import models


class Game(models.Model):
    download = models.FileField(blank=True, null=True, upload_to='versions')


class Post(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='game')
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.created} - {self.name}"

    class Meta:
        ordering = ['created', 'name']


class Version(models.Model):
    slug = models.CharField(max_length=255, unique=True, blank=True)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.slug} - {self.created}"

    class Meta:
        ordering = ['created']

