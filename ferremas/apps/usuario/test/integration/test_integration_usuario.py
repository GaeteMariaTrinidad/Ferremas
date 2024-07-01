import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.usuario.models import Usuario

@pytest.mark.django_db
class TestUsuarioAPI(APITestCase):

    def setUp(self):
        self.url_list_create = reverse('usuario-list-create')
        self.usuario_data = {
            'nombre': 'Benjamin',
            'apellido': 'Morales',
            'contrasena': '12345',
            'correo': 'correo@prueba.com',
            'edad': 25,
        }

    def test_create_usuario(self):
        response = self.client.post(self.url_list_create, self.usuario_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Usuario.objects.count() == 1
        assert Usuario.objects.get().nombre == 'Benjamin'

    def test_create_usuario_invalid_data(self):
        invalid_data = self.usuario_data.copy()
        invalid_data['correo'] = 'invalidemail'  
        response = self.client.post(self.url_list_create, invalid_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Usuario.objects.count() == 0

    def test_get_usuario(self):
        usuario = Usuario.objects.create(**self.usuario_data)
        url = reverse('usuario-detail', args=[usuario.pk])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['nombre'] == self.usuario_data['nombre']

    def test_update_usuario(self):
        usuario = Usuario.objects.create(**self.usuario_data)
        updated_data = {
            'nombre': 'Trinidad',
            'apellido': 'Gaete',
            'contrasena': 'prueba123',
            'correo': 'actualizado@prueba.com',
            'edad': 35,
        }
        url = reverse('usuario-detail', args=[usuario.pk])
        response = self.client.put(url, updated_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        usuario.refresh_from_db()
        assert usuario.nombre == updated_data['nombre']

    def test_delete_usuario(self):
        usuario = Usuario.objects.create(**self.usuario_data)
        url = reverse('usuario-detail', args=[usuario.pk])
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Usuario.objects.count() == 0

    def test_delete_usuario_not_found(self):
        url = reverse('usuario-detail', args=[999]) 
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
