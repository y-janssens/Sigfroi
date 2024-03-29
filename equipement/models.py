from django.db import models
from utils.choices import NOTES, WEAPONTYPE, TYPE, AREA


class Armor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(
        max_length=50, choices=TYPE, default='Type', blank=True, null=True)
    text = models.TextField(max_length=2000, blank=True, null=True)
    areas = models.CharField(
        max_length=50, choices=AREA, default='Zone', blank=True, null=True)
    protection = models.IntegerField(blank=True, null=True)
    note = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['type', 'name']


class Weapon(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(
        max_length=50, choices=WEAPONTYPE, default='Type', blank=True, null=True)
    text = models.TextField(max_length=2000, blank=True, null=True)
    damages = models.CharField(max_length=50, blank=True, null=True)
    parry = models.IntegerField(blank=True, null=True)
    penalty = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['type', 'name']


class StuffSheet(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, null=True, editable=False)
    armor = models.ForeignKey(
        Armor, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    weapon = models.ForeignKey(
        Weapon, on_delete=models.CASCADE, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.owner.name} - {self.weapon.name if self.weapon else self.armor.name}'

    class Meta:
        unique_together = [['owner', 'armor', 'weapon']]
        ordering = ['weapon', 'armor']


class CustomSheet(models.Model):
    owner = models.ForeignKey(
        'fiches.CharacterSheet', on_delete=models.CASCADE, blank=True, null=True, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.owner.name} - {self.name}'

    class Meta:
        ordering = ['name']


class ArmoryWeaponsNote(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=2000, blank=True, null=True)
    type = models.CharField(
        max_length=50, choices=NOTES, default='list', blank=True, null=True)

    def __str__(self):
        return self.name or self.title

    class Meta:
        ordering = ['-type', 'name', 'title']
