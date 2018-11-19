from django import forms
from Apps.Banco.models import Personal

class PersonalForm(forms.ModelForm):

    class Meta:
        model = Personal

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'sexo',
            'universidad',
            'profesion',
            'especialidad',
            'año_egreso',
        ]

        labels = {
            'nombre': 'Nombres Completos',
            'apellidos': 'Apellidos Completos',
            'edad': 'Edad',
            'sexo': 'Sexo',
            'universidad': 'Universidad',
            'profesion': 'Profesion',
            'especialidad': 'Especialidad',
            'año_egreso': 'Año Egreso',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'apellidos': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'edad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'sexo': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'universidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'profesion': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'especialidad': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'año_egreso': forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }