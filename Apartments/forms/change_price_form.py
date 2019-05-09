from django.forms import widgets
from django import forms

class ChangePriceForm(forms.Form):
    price = forms.FloatField()
