from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer

from .models import Usuario
# Create your views here.
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


def create_Usuario(nombreU, apellidoU,contrasenaU,correoU,edadU): 
    usuario =  Usuario.objects.create(nombre=nombreU, apellido=apellidoU,contrasena=contrasenaU,correo=correoU,edad=edadU)
    
    return usuario



def get_Usuario(ID):
    ob = Usuario.objects.get(id=ID)
    print(ob)
    return ob



def update_correo_user(user, contra,newCorreo):
   # Buscar el producto por código si no se proporciona directamente

    ob = Usuario.objects.get(contrasena=contra)

    # Actualizar el precio del producto
    print(ob)
    ob.correo = newCorreo
    ob.save()

    return ob    
    
def delete_user(user):
    user.delete()