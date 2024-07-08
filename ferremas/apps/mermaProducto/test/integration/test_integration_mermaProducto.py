import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.mermaProducto.models import Producto
from apps.producto.views import create_producto

from datetime import datetime

@pytest.mark.django_db
class TestmermaProductoAPI(APITestCase):
    def setUp(self):
        self.prod = create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        self.url = reverse('mermaProducto_list_create')
        self.producto_data = {
            'producto': self.prod.id,  # Usamos el ID del producto aquí
            'detalle_merma': '11',
            'fecha': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),  # Formateamos la fecha a formato JSON
            'valorPerdida': 5000,
        }

    def test_create_mermaProducto(self):
        response = self.client.post(self.url, self.producto_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Producto.objects.count() == 1

    def test_create_mermaProducto_invalid_data(self):
        initial_count = Producto.objects.count()  # Contar productos inicialmente
        prod = create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        invalid_data = {
            'producto': prod.id,  # Usamos el ID del producto aquí
            'detalle_merma': '11',  # Aquí está la data inválida porque debería ser un string
            'fecha': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'valorPerdida': '5000x',
        }
        response = self.client.post(self.url, invalid_data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Producto.objects.count() == initial_count  # Verificar que el conteo de productos no ha cambiado

    def test_get_mermaProducto(self):
        merma_producto = Producto.objects.create(
            producto=self.prod,
            detalle_merma='11',
            fecha=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            valorPerdida=5000,
        )
        url = reverse('mermaProducto_detail', args=[merma_producto.pk])
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['detalle_merma'] == '11'

    def test_get_mermaProducto_not_found(self):
        url = reverse('mermaProducto_detail', args=[999])  # ID no existente
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_404_NOT_FOUND