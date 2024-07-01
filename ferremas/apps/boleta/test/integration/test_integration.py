import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from apps.boleta.models import Boleta

@pytest.mark.django_db
class TestBoletaIntegration:
    def setup_method(self):
        self.client = APIClient()
        self.boleta_data = {
            'total': 24890,
            'fecha': datetime.now().isoformat(),
            'cliente': 'Benjamin Morales',
            'productosVendidos': 'Taladro percutor Bauker, Caja tornillos',
            'numBoleta': 1
        }

    def test_create_boleta(self):
        url = reverse('boleta_list_create')  
        response = self.client.post(url, self.boleta_data, format='json')
        assert response.status_code == 201
        assert Boleta.objects.count() == 1

    def test_get_boleta(self):
        boleta = Boleta.objects.create(**self.boleta_data)
        url = reverse('boleta_detail', args=[boleta.numBoleta])
        response = self.client.get(url, format='json')
        assert response.status_code == 200
        assert response.data['numBoleta'] == boleta.numBoleta

    def test_update_boleta(self):
        boleta = Boleta.objects.create(**self.boleta_data)
        url = reverse('boleta_detail', args=[boleta.numBoleta])
        updated_data = self.boleta_data.copy()
        updated_data['total'] = 49640
        response = self.client.put(url, updated_data, format='json')
        assert response.status_code == 200
        boleta.refresh_from_db()
        assert boleta.total == 49640

    def test_delete_boleta(self):
        boleta = Boleta.objects.create(**self.boleta_data)
        url = reverse('boleta_detail', args=[boleta.numBoleta])
        response = self.client.delete(url, format='json')
        assert response.status_code == 204
        assert Boleta.objects.count() == 0
