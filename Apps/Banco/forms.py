from django.forms import ModelForm
from django import forms
from Apps.Banco.models import Banco
#choice = (('0','no'),('1','Si'))
class BancoForm(ModelForm):

    class Meta:
        model = Banco

        fields = '__all__'

        labels = {
            'nombre': 'Nombre del Banco',
            'pais': 'Nombre del Pais',
            'ruc': 'Numero de RUC',
            'fk_egresos': 'Egresos Netos',
            'fk_ingresos': 'Ingresos Netos',
            'fk_personal': 'Nombre del Personal',
            'user': 'Usuario',
            'auditor': 'Auditor',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'pais': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'ruc': forms.TextInput(attrs={'class':'form-control', 'required':''}),
            'fk_egresos': forms.Select(attrs={'class':'form-control', 'required':''}),
            'fk_ingresos': forms.Select(attrs={'class':'form-control', 'required':''} ),
            'fk_personal': forms.Select(attrs={'class':'form-control', 'required':''} ),
            'user': forms.Select(attrs={'class':'form-control', 'required':''} ),
            'auditor': forms.Select(attrs={'class':'form-control', 'required':''} ),
        }