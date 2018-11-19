from django import forms
from Apps.Banco.models import Ingresos

class IngresosForm(forms.ModelForm):

    class Meta:
        model = Ingresos

        fields = [
            'ingresos',
            'porcentaje',
            'ingresos_neto',
        ]

        labels = {
            'ingresos': 'Ingrese Ingresos',
            'porcentaje': 'Procentaje (disminucion)',
            'ingresos_neto': 'Ingresos Netos',
        }

        widgets = {
            'ingresos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': '',
                }
            ),
            'porcentaje': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'ingresos_neto': forms.TextInput(attrs={'class':'form-control', 'required':''}),
        }