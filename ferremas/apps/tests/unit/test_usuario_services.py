import pytest
from django.contrib.auth.models import User

from apps.usuario.services import create_user, delete_user, get_user


@pytest.mark.django_db
class TestUsuarioService:
    def test_create_user_succesfully(self):
        """
        Se recomienda colocar una descripción de lo que debe realizar la prueba, 
        para este caso vamos a validar que el método crear usuario funcione correctamente, 
        adicionalmente, si desean, pueden agregar comentarios del paso a paso
        """
        # Creamos un usuario nuevo
        user = create_user('testuser', 'testpassword')
        
        # Verificamos que el usuario creado tenga el mismo username que usamos para crearlo
        assert user.username == 'testuser'

        # Verificamos con el método check_password que la contrase;a sea correcta
        assert user.check_password('testpassword') is True
        
    def test_delete_user_successfully(self):
        # Creamos un usuario nuevo para eliminarlo posteriormente
        user = create_user('testuser', 'testpassword')

        # Eliminamos nuestro usuario
        delete_user(user)

        # Validamos que el usuario ya no exista dentro de nuestra base de datos de prueba
        with pytest.raises(User.DoesNotExist):
            get_user(user.id)
