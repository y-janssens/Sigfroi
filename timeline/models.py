from django.db import models


class TimelineLink(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    text = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class TimelineEvent(models.Model):
    name = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    details = models.TextField(max_length=30000, blank=True, null=True)
    consequences = models.TextField(max_length=30000, blank=True, null=True)
    links = models.ManyToManyField(TimelineLink, blank=True, symmetrical=False)

    def __str__(self):
        return f"{self.date} {self.year} - {self.title}"

    class Meta:
        ordering = ['year', 'name']
