from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    codigo = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.precio}"
    
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} - {self.cantidad} - {self.herramienta.nombre} - {self.id} - {self.herramienta.precio}"
    

 