from django.db import models
from apps.producto.models import Producto 
from apps.usuario.models import  Usuario
# Create your models here.
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.cantidad} - {self.producto.nomre} - {self.id} - {self.producto.precio}"