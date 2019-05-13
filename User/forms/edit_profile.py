from django.contrib.auth.models import User
from User.models import ProfileImage
from django.forms import ModelForm, widgets
from django import forms

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        exclude = ['id', 'username', 'password']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
        }

class EditImageForm(forms.ModelForm):
    image = forms.CharField()
    class Meta:
        model = ProfileImage
        fields = ('img',)
        exclude = ['id', 'user']
        widgets = {
            'img': widgets.TextInput(attrs={'class': 'form-control'}),
        }