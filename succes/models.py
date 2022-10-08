from django.db import models
from fiches.models import CharacterSheet


class Achievement(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        ordering = ['id']


class AchievementsSheet(models.Model):
    achievements = Achievement.objects.all()
    owner = models.ForeignKey(
        CharacterSheet, on_delete=models.CASCADE, blank=True, editable=False)

    for achievement in achievements:
        locals()[achievement.title] = models.BooleanField(
            default=False, blank=False, null=False)

    def __str__(self):
        return self.owner.name

    class Meta:
        ordering = ['owner']
