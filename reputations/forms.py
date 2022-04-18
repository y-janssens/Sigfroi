from django import forms
from django.forms import ModelForm
from .models import *


class PeopleReputationForm(ModelForm):
    class Meta:
        model = PeopleReputation
        fields = '__all__'


class NobilityReputationForm(ModelForm):
    class Meta:
        model = NobilityReputation
        fields = '__all__'


class MilitiaReputationForm(ModelForm):
    class Meta:
        model = MilitiaReputation
        fields = '__all__'


class ClergyReputationForm(ModelForm):
    class Meta:
        model = ClergyReputation
        fields = '__all__'


class BanishedReputationForm(ModelForm):
    class Meta:
        model = BanishedReputation
        fields = '__all__'
