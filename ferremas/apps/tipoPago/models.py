from django.db import models
from apps.boleta.models import Boleta
# Create your models here.

class Pago(models.Model):
    TipoPago = models.CharField(max_length=100)
    TotalCompra =models.IntegerField()
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.TipoEntrega} - {self.Valor}"