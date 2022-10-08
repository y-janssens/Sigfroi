from django.contrib import admin
from .models import TimelineEvent, TimelineLink

admin.site.register(TimelineLink)
admin.site.register(TimelineEvent)
