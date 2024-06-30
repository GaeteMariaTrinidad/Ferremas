from django.urls import path
from . import views

urlpatterns = [
    path('/',views.ProductoListCreate.as_view(), name='productos-list-create'),
    path('/<int:pk>/',views.ProductoDetail.as_view(), name='producto-detail')
]
