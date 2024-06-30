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


def create_producto(productName, productMarca,Stock,Codigo,Precio): 
    producto =  Producto.objects.create(nomre=productName, marca=productMarca,stock=Stock,codigo=Codigo,precio=Precio)
    
    return producto

def get_producto(producto_codigo):
    ob = Producto.objects.get(codigo=producto_codigo)
    print(ob)
    return ob



def update_precio_producto(producto, codigo,NewPrecio):
   # Buscar el producto por código si no se proporciona directamente

    ob = Producto.objects.get(codigo=codigo)

    # Actualizar el precio del producto
    print(ob)
    ob.precio = NewPrecio
    ob.save()

    return ob    
    
def delete_producto(producto):
    producto.delete()