import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status  

@pytest.mark.django_db
class TestAccountAPI:
    def test_user_registration_succesfully(self):
        client = APIClient()
        url = reverse("nombre_url") 

data = {
    'username': 'testuser',
    'password': 'testpassword123'
}        

response = client.post(url, data, format='json')

assert response.status_code == status.HTTP_201_CREATED
assert 'username' in response.data
# assert response.data []
