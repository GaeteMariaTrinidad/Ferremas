from rest_framework import serializers
from .models import  carrito
from apps.producto.serializers  import ProductoSerializer


class CarritoSerializer(serializers.ModelSerializer):
    Producto = ProductoSerializer()

    class Meta:
        model = carrito
        fields = ['id', 'usuario', 'herramienta', 'cantidad']