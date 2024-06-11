# myapp/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('Herraminetas/', views.ItemListCreate.as_view(), name='item-list-create'),
    path('Herramineta/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('carrito_list/', views.CarritoView.as_view(), name='carrito-List'),
    path('carrito_add/', views.CarritoView.as_view(), name='carrito-add'),
    path('carrito_delete/<int:id>/', views.CarritoView.as_view(), name='carrito-delete'),
    path('pagar_carrito/', views.PagarCarritoAPIView.as_view(), name='pagar_carrito'),
]

