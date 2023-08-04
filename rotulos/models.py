from django.db import models
from django.utils import timezone

from clientes.models import Cliente

class Rotulo(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_rotulo = models.CharField(max_length=255, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(blank=True, null=True)
    valor_cobrado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_recebido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    documentacao = models.BooleanField(default=False)
    