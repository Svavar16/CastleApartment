from django.forms import ModelForm, widgets
from django import forms
from Apartments.models import Apartments


class ApartmentsCreateForm(ModelForm):
    image = forms.CharField(required=True)

    class Meta:
        model = Apartments
        exclude = ['id']
        widgets = {
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'address': widgets.Select(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'privateEntrance': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'animalsAllowed': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'garage': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'yearBuild': widgets.NumberInput(attrs={'class': 'form-control'}),
            'sellerID': widgets.Select(attrs={'class': 'form-control'}),
        }
