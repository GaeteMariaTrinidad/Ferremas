from django.urls import path
from .views import BoletaListCreate, BoletaDetail

urlpatterns = [
    path('boleta/', BoletaListCreate.as_view(), name='boleta_list_create'),
    path('boleta/<int:pk>/', BoletaDetail.as_view(), name='boleta_detail'),
]