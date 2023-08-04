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

    @property
    def status(self):
        if self.documentacao and self.valor_recebido is None and self.data_entrega is None:
            return "Confeccionar"
        elif not self.documentacao and self.valor_recebido is None and self.data_entrega is None:
            return "Pendente"
        elif self.documentacao and self.valor_recebido is not None and self.data_entrega is None:
            return "Entregar"
        elif self.documentacao and self.valor_recebido is not None and self.data_entrega is not None:
            return "Entregue"
