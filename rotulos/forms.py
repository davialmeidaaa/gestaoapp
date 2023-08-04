from django import forms
from .models import Rotulo
from clientes.models import Cliente

class RotuloForm(forms.ModelForm):
    class Meta:
        model = Rotulo
        exclude = ['data_criacao']

    def __init__(self, *args, **kwargs):
        super(RotuloForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
