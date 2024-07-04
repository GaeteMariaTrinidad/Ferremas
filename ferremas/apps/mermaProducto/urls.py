from django.urls import path
from .views import MermaProductoListCreate, MermaProductoDetail

urlpatterns = [
    path('mermaProducto/', MermaProductoListCreate.as_view(), name='mermaProducto_list_create'),
    path('mermaProducto/<int:pk>/', MermaProductoDetail.as_view(), name='mermaProducto_detail'),
]