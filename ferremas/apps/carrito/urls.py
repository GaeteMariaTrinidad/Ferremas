from django.urls import path
from . import views

urlpatterns = [
    
    path('carrito_list/',views.CarritoView.as_view(), name='carrito-List'),
    path('carrito_add/',views.CarritoView.as_view(), name='carrito-add'),
    path('carrito_delete/<int:id>/',views.CarritoView.as_view(), name='carrito-delete'),
    path('pagar_carrito/',views.PagarCarritoAPIView.as_view(), name='pagar_carrito'),
]
