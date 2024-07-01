from django.urls import path
from .views import BoletaListCreate, BoletaDetail

urlpatterns = [
    path('boletas/', BoletaListCreate.as_view(), name='boleta_list_create'),
    path('boletas/<int:pk>/', BoletaDetail.as_view(), name='boleta_detail'),
]