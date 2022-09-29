from django import forms
from django.forms import ModelForm
from .models import *


class SnapshotUploadForm(ModelForm):
    class Meta:
        model = Snapshot
        fields = '__all__'
