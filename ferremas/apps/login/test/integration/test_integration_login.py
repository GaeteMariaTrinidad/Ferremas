import pytest
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.usuario.models import Usuario

class TestProductoAPI(APITestCase):
    def setUp(self):
        self.url = reverse('login')  # Asegúrate de tener 'login' como el nombre de la URL para esta vista
        self.usuario = Usuario.objects.create(
            nombre='Usuario',
            apellido='apellido',
            contrasena='12345',
            correo='correo@correo.com',
            edad=25,
        )
        self.login_data = {
            'correo': self.usuario.correo,
            'contrasena': '12345',
        }
    def test_login_valid(self):
        
        # Realizar la solicitud de login
        response = self.client.post(self.url, self.login_data, format='json')

        # Verificar que se devuelve un código de estado HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar el contenido de la respuesta
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], "Login successful")
        self.assertIn('user_id', response.data)
        self.assertEqual(response.data['user_id'], self.usuario.id)

    def test_login_invalid_all_data(self):
        invalid_data = {}  
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['correo'][0], "This field is required.")


    def test_login_invalid_user_data(self):
        invalid_data = {
            'correo': 'correo@inexistente.com',
            'contrasena': 'contraseñaincorrecta',
        }
       
        response = self.client.post(self.url, invalid_data, format='json')

        # Verificar que se devuelve un código de estado HTTP 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verificar que se devuelve el mensaje de error esperado
        self.assertEqual(response.data['non_field_errors'][0], "Usuario no encontrado.")

    def test_login_invalid_pass_data(self):
        # Crear un usuario de prueb
        invalid_data = {
            'correo':'correo@correo.com',
            'contrasena': 'contraseñaIncorrecta',
        }
        response = self.client.post(self.url, invalid_data, format='json')

        # Verificar que se devuelve un código de estado HTTP 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verificar que se devuelve el mensaje de error esperado
        self.assertEqual(response.data['non_field_errors'][0], "Contraseña incorrecta.")
