# myapp/urls.py
from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path('/productos/',include('apps.producto.urls')),
    path('/carritos/',include('apps.carrito.urls')),
    path('/usuarios/',include('apps.usuario.urls'))
]

