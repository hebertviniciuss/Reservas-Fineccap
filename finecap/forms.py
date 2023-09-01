from django.forms import ModelForm
from django import forms
from .models import Stand, Reserva


class StandForm(ModelForm):
   
    class Meta:
        model = Stand
        fields = '__all__'
        widgets = {
        'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
        'valor': forms.NumberInput(attrs={'class': 'form-control'})
        }


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