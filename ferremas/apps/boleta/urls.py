from django.urls import path
from . import views

urlpatterns = [
    path('/',views.BoletaListCreate.as_view(), name='productos-list-create'),
    path('/<int:pk>/',views.BoletaDetail.as_view(), name='producto-detail')
]