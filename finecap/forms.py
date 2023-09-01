from django import forms
from .models import Stand, Reserva


class StandForm(forms.ModelForm):
   
    class Meta:
        model = Stand
        fields = '__all__'
        widgets = {
        'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
        'valor': forms.NumberInput(attrs={'class': 'form-control'})
        }


class ReservaForm(forms.ModelForm):
   
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
        'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        'categoria': forms.TextInput(attrs={'class': 'form-control'}),
        'stand': forms.Select(attrs={'class': 'form-control'}),
        'quitado': forms.RadioSelect(attrs={'class': 'form-control'}),
        }