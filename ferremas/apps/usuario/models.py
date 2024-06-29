from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    edad =  models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.id}"