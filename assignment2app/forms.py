from django import forms
from .models import *


class Casino(forms.ModelForm):
    class Meta:
        model= CasinoModel
        exclude = []

class TableGame(forms.ModelForm):
    class Meta:
        model= TableGameModel
        exclude = []

class Restaurant(forms.ModelForm):
    class Meta:
        model= RestaurantModel
        exclude = []
