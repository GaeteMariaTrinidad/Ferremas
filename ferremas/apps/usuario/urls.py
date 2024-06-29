from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.UsuarioListCreate.as_view(), name='usuario-list-create')
]
