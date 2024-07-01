import pytest
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.carrito.models import Carrito
from apps.producto.models import Producto
from apps.usuario.models import Usuario

@pytest.mark.django_db
class TestCarritoAPI:
    def setup_method(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(nombre='Usuario', apellido='Prueba', contrasena='12345', correo='correo@correo.com', edad=29)
        self.producto = Producto.objects.create(nomre='Producto Prueba', marca='Bauker', stock=5, codigo='001', precio=4990)
        self.carrito_data = {
            'usuario_id': self.usuario.id,
            'producto_id': self.producto.id,
            'cantidad': 2
        }

    def test_create_carrito_api_successfully(self):
        url = reverse('carrito-add')
        usuario = Usuario.objects.create(nombre='Usuario Prueba', apellido='Apellido', contrasena='12345', correo='correo@correo.com', edad=30)
        producto = Producto.objects.create(nomre='Producto Prueba', marca='Bauker', stock=10, codigo='001', precio=4990)

        data = {
            'usuario_id': usuario.id,
            'producto_id': producto.id,
            'cantidad': 2
        }
        
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Carrito.objects.count(), 1)

        #assert response.status_code == status.HTTP_201_CREATED
        #assert Carrito.objects.count() == 1

        #carrito_creado = Carrito.objects.first()
        #assert carrito_creado.id == Carrito.id
        #assert carrito_creado.producto == producto.id
        #assert carrito_creado.cantidad == data['cantidad']

    def test_get_carrito_api_successfully(self):
        carrito = Carrito.objects.create(**self.carrito_data)
        url = reverse('carrito-List')
        
        response = self.client.get(url, format='json')
        response.data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Success'  # Verifica el mensaje de éxito esperado
        assert 'Articulos del Carrito' in response.data  # Verifica la presencia de 'Articulos del Carrito'
        assert len(response.data['Articulos del Carrito']) == 1


    def test_update_carrito_api_successfully(self):
        carrito = Carrito.objects.create(**self.carrito_data)
        updated_data = self.carrito_data.copy()
        updated_data['cantidad'] = 3
        url = reverse('carrito-delete', args=[carrito.id])
        
        response = self.client.post(url, updated_data, format='json')
        
        assert response.status_code == status.HTTP_200_OK
        carrito.refresh_from_db()
        assert carrito.cantidad == 3

    def test_delete_carrito_api_successfully(self):
        carrito = Carrito.objects.create(**self.carrito_data)
        url = reverse('carrito-delete', args=[carrito.id])
        
        response = self.client.delete(url, format='json')
        
        assert response.status_code == status.HTTP_200_OK 
        assert Carrito.objects.count() == 0

    def test_pagar_carrito_api_successfully(self):
        print(f"Usuario ID: {self.usuario.id}, Producto ID: {self.producto.id}")  # Depuración
        carrito = Carrito.objects.create(usuario=self.usuario, producto=self.producto, cantidad=3)
        
        url = reverse('pagar_carrito')
        data = {'id_carrito': carrito.id, 'confirmacion': 'si'} 
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'OK'
        assert 'Detalle venta' in response.data  
        assert 'Pago' in response.data 


    def test_pagar_carrito_empty_api_successfully(self):
        carrito = Carrito.objects.create(usuario=self.usuario, producto=self.producto, cantidad=0)
        url = reverse('pagar_carrito')
        data = {'id_carrito': carrito.id, 'confirmacion': 'no'}  
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Success'
        assert 'El Carrito esta vacio' in response.data['message']

