import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.boleta.models import Boleta
from datetime import datetime

@pytest.mark.django_db
class TestBoletaAPI:
    def setup_method(self):
        self.client = APIClient()
        self.boleta_data = {
            'total': 49980,
            'fecha': datetime.now(),
            'cliente': 'Benjamin Morales',
            'productosVendidos': 'Taladro percutor Bauker, Caja tornillos',
            'numBoleta': 1
        }

    def test_create_boleta_api_successfully(self):
        """
        Prueba que se pueda crear una boleta por medio de la API
        """
        url = reverse('boleta_list_create') 

        response = self.client.post(url, self.boleta_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Boleta.objects.count() == 1

    def test_get_boleta_api_successfully(self):
        """
        Prueba que se pueda obtener una boleta por medio de la API
        """
        boleta = Boleta.objects.create(**self.boleta_data)
        url = reverse('boleta_detail', args=[boleta.numBoleta])

        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['numBoleta'] == boleta.numBoleta

    def test_update_boleta_api_successfully(self):
        """
        Prueba que se pueda actualizar una boleta por medio de la API
        """
        boleta = Boleta.objects.create(**self.boleta_data)
        url = reverse('boleta_detail', args=[boleta.numBoleta])

        updated_data = self.boleta_data.copy()
        updated_data['total'] = 46460

        response = self.client.put(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        boleta.refresh_from_db()
        assert boleta.total == 46460

    def test_delete_boleta_api_successfully(self):
        """
        Prueba que se pueda eliminar una boleta por medio de la API
        """
        boleta = Boleta.objects.create(**self.boleta_data)
        url = reverse('boleta_detail', args=[boleta.numBoleta])

        response = self.client.delete(url, format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Boleta.objects.count() == 0
