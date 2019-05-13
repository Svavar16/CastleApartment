from django import forms
from django.forms import widgets
from User.models import CardDetails


class SelectCardForm(forms.Form):
    CardSelect = forms.ModelChoiceField(queryset=None)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(SelectCardForm, self).__init__(*args, **kwargs)

        self.fields['CardSelect'].queryset = CardDetails.objects.filter(owner=self.user)
