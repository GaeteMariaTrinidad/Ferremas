from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.producto.models import Producto

class TestProductoAPI(APITestCase):

    def setUp(self):
        self.url = reverse('productos-list-create')
        self.producto_data = {
            'nomre': 'Producto de prueba',
            'marca': 'Bauker',
            'stock': 5,
            'codigo': '001',
            'precio': 4990,
        }

    def test_create_producto(self):
        response = self.client.post(self.url, self.producto_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Producto.objects.count() == 1

    def test_create_producto_invalid_data(self):
        invalid_data = {
            'nomre': 'Producto de prueba',
            'marca': 'Makita',
            'stock': 'invalid',  
            'codigo': '002',
            'precio': 4590,
        }
        response = self.client.post(self.url, invalid_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Producto.objects.count() == 0

    def test_get_producto(self):
        producto = Producto.objects.create(**self.producto_data)
        url = reverse('producto-detail', args=[producto.pk])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['nomre'] == self.producto_data['nomre']

    def test_get_producto_not_found(self):
        url = reverse('producto-detail', args=[999])  # ID no existente
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_404_NOT_FOUND
