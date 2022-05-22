from django.contrib import admin
from .models import Aliase, AliasesSheet, CharacterSheet

admin.site.register(CharacterSheet)
admin.site.register(AliasesSheet)
admin.site.register(Aliase)
