from django import forms
from Apps.Banco.models import Egresos

class EgresosForm(forms.ModelForm):
    
    class Meta:
        model = Egresos

        fields = [
            'egresos',
            'porcentaje',
            'egresos_neto',
        ]

        labels = {
            'egresos': 'Egresos',
            'porcentaje': 'Procentaje (aumento)',
            'egresos_neto': 'Egresos Neto',
        }

        widgets = {
            'egresos': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'porcentaje': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'egresos_neto': forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }