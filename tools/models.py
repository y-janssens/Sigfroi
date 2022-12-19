from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from choices import COLORS


class ProgressBar(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50, choices=COLORS, default="default")
    total = models.IntegerField(default=100)
    symbol = models.CharField(max_length=10, default="%")
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
