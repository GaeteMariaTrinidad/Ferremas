from django.shortcuts import render
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import generics
# Create your views here.

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
