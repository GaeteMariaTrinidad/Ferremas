from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer

from .models import Usuario
# Create your views here.
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer