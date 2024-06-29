from django.db import models
from apps.producto.models import  Producto
class Producto(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    detalle_merma = models.CharField(max_length=500)
    fecha = models.DateTimeField()
    valorPerdida = models.IntegerField()
    def __str__(self):
        return f"{self.producto} - {self.detalle_merma}"