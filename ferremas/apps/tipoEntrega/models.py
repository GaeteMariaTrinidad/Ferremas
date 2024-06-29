from django.db import models

# Create your models here.
class Entrega(models.Model):
    TipoEntrega = models.CharField(max_length=100)
    Valor =models.IntegerField()
    courier = models.CharField(max_length=100)
    articulos = models.IntegerField()
    def __str__(self):
        return f"{self.TipoEntrega} - {self.Valor}"