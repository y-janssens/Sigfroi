from django.contrib import admin
from .models import Armor, Weapon, StuffSheet, ArmoryWeaponsNote, CustomSheet

admin.site.register(Armor)
admin.site.register(Weapon)
admin.site.register(StuffSheet)
admin.site.register(CustomSheet)
admin.site.register(ArmoryWeaponsNote)
