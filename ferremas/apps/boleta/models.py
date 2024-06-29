from django.db import models

# Create your models here.
class Boleta(models.Model):
    total =  models.IntegerField()
    fecha = models.DateTimeField()
    cliente =  models.CharField(max_length=50)
    productosVendidos = models.CharField(max_length=50)
    numBoleta = models.IntegerField()

    def __str__(self):
        return f"{self.total} - {self.fecha}"