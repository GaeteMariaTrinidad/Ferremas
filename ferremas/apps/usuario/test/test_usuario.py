import pytest
from apps.usuario.views import create_Usuario,get_Usuario,update_correo_user,delete_user


@pytest.mark.django_db
class TestUsuarioService:
    def test_create_usuario_succesfully(self):
        """
         vamos a validar que el método crear usuario funcione correctamente

        """
        user = create_Usuario('benjamin', 'morales', 'ben123', 'benjamorales874@gmail.com', '25')
    
        # Verificamos que el usuario creado tenga el mismo username que usamos para crearlo
        assert user.nombre == 'benjamin'

    def test_geId_usuario_succesfully(self):
        """
         vamos a validar que el método traiga la informacion de un usuario por id

        """
        create_Usuario('benjamin', 'morales', 'ben123', 'benjamorales874@gmail.com', '25')
        id = '1'
        usuario = get_Usuario(id)
        assert usuario.id ==1

    def test_update_usuario_succesfully(self):
        """
         vamos a validar que el método cambie de correo segun id del usuario

        """
        create_Usuario('benjamin', 'morales', 'ben123', 'benjamorales874@gmail.com', '25')
        id = '1'
        
        update_correo_user('benjamin','ben123','benja4@gmail.com')
        producto = get_Usuario(id)

        assert producto.correo == 'benja4@gmail.com'


    def test_delete_usuario_succesfully(self):
        """
         vamos a validar que el método elimine segun el usuario

        """
        usuario = create_Usuario('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        
        delete_user(usuario)
        # Validamos que el usuario ya no exista dentro de nuestra base de datos de prueba
        with pytest.raises(usuario.DoesNotExist):
            get_Usuario(usuario.id)