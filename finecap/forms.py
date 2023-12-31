from django.forms import ModelForm
from django import forms
from .models import Reserva

class ReservaForm(ModelForm):
   
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
        'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        'categoria': forms.TextInput(attrs={'class': 'form-control'}),
        'stand': forms.Select(attrs={'class': 'form-control'}),
        }