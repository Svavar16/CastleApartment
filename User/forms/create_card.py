from django.forms import ModelForm, widgets
from User.models import CardDetails


class CreateCardForm(ModelForm):
    class Meta:
        model = CardDetails
        exclude = ['id', 'owner']
        widgets = {
            'firstName': widgets.TextInput(attrs={'class': 'form-control'}),
            'lastName': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'dateOfExpire': widgets.DateInput(attrs={'class': 'form-control'}),
            'CVV': widgets.TextInput(attrs={'class': 'form-control'})
        }
