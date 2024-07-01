from django.shortcuts import render
from .models import Boleta
from .serializers import BoletaSerializer
from rest_framework import generics
from django.views.generic import DetailView

# Create your views here.

class BoletaListCreate(generics.ListCreateAPIView):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class BoletaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class BoletaDetailView(DetailView):
    model= Boleta
    template_name = 'boleta/boleta_detail.html'  

class BoletaListCreateView(DetailView):
    model= Boleta
    template_name = 'boleta/boleta_list_create.html'       


def create_boleta(Total, Fecha, Cliente, ProductosVendidos, NumBoleta): 
    boleta =  Boleta.objects.create(total=Total, fecha=Fecha, cliente=Cliente, productosVendidos=ProductosVendidos, numBoleta=NumBoleta)
    
    return boleta
 
def get_boleta(boleta_numBoleta):
    try:
        boleta = Boleta.objects.get(numBoleta=boleta_numBoleta)
        print(boleta)
        return boleta
    except Boleta.DoesNotExist:
        print(f"No se encontró una boleta con el número {boleta_numBoleta}")
        return None
    
def delete_boleta(boleta):
    boleta.delete()

def update_boleta(boleta_numBoleta, **kwargs):
    try:
        boleta = Boleta.objects.get(numBoleta=boleta_numBoleta)
        for key, value in kwargs.items():
            if hasattr(boleta, key):
                setattr(boleta, key, value)
        boleta.save()
        return boleta
    except Boleta.DoesNotExist:
        print(f"No se encontró una boleta con el número {boleta_numBoleta}")
        return None    