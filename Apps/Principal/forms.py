from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm):

    class Meta:
        model = User

        fields = [
            'password',
            'username',
            
        ]

        labels = {
            'password': 'Contraseña',
            'username': 'Nombre de usuario',
            
        }

        widgets = {
            'password': forms.TextInput(attrs={'class':'control-form'}),
            'username': forms.TextInput(attrs={'class':'control-form'}),
            
        }