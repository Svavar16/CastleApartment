from django.forms import ModelForm, widgets
from django import forms
from Apartments.models import Apartments, Location


class ApartmentsCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    locationApartment = forms.NumberInput()

    class Meta:
        model = Apartments
        exclude = ['id', 'locationID', 'forSale', 'sellerID']
        widgets = {
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'privateEntrance': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'animalsAllowed': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'garage': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
            'yearBuild': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'})
        }


class LocationCreateForm(ModelForm):

    class Meta:
        model = Location
        exclude = ['id']
        widgets = {
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postalCode': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
