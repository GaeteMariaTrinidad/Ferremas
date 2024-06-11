from rest_framework import serializers
from .models import Herramienta, Carrito

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Herramienta
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    herramienta = ItemSerializer()

    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'herramienta', 'cantidad']