from django.forms import ModelForm
from .models import Card, CardSheet


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


class CardSheetForm(ModelForm):
    class Meta:
        model = CardSheet
        fields = '__all__'
