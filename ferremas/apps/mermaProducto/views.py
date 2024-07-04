from django.shortcuts import render
from .models import Producto
from .serializers import MermaProductoSerializer
from rest_framework import generics 
from django.views.generic import DetailView

# Create your views here.

class MermaProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = MermaProductoSerializer

class MermaProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = MermaProductoSerializer

class MermaProduoctoDetailView(DetailView):
    model= Producto
    template_name = 'mermaProducto/mermaProducto_detail.html'  

class MermaProductoListCreateView(DetailView):
    model= Producto
    template_name = 'mermaProducto/mermaProducto_list_create.html'

def create_mermaProducto(Producto1, Detalle_merma, Fecha, ValorPerdida): 
    mermaProducto =  Producto.objects.create(producto=Producto1, detalle_merma=Detalle_merma, fecha=Fecha, valorPerdida=ValorPerdida)
    
    return mermaProducto
 
def get_mermaProducto(producto_numMermaProducto):
    try:
        mermaProduto = Producto.objects.get(detalle_Merma=producto_numMermaProducto)
        print(mermaProduto)
        return mermaProduto
    except mermaProduto.DoesNotExist:
        print(f"No se encontró una merma del producto {producto_numMermaProducto}")
        return None
    
def delete_mermaProducto(mermaProducto):
    mermaProducto.delete()

def update_mermaProducto(mermaProducto_numMermaProducto, **kwargs):
    try:
        mermaProducto = Producto.objects.get(detalle_merma=mermaProducto_numMermaProducto)
        for key, value in kwargs.items():
            if hasattr(mermaProducto, key):
                setattr(mermaProducto, key, value)
        mermaProducto.save()
        return mermaProducto
    except mermaProducto.DoesNotExist:
        print(f"No se encontró una merma del producto {mermaProducto_numMermaProducto}")
        return None    