from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'nome_fantasia',
            'cnpj',
            'endereco',
            'numero',
            'complemento',
            'cep',
            'bairro',
            'cidade',
            'uf',
            'email',
            'telefone'
        ]
