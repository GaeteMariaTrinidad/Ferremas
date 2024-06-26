from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nomre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField()
    codigo = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.nomre} - {self.precio} - {self.codigo} - {self.id}"