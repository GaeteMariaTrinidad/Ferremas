import pytest
from apps.producto.views import create_producto,get_producto,update_precio_producto,delete_producto


@pytest.mark.django_db
class TestProductoService:
    def test_create_producto_succesfully(self):
        """
         vamos a validar que el método crear producto funcione correctamente

        """
        producto = create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
    
        # Verificamos que el usuario creado tenga el mismo username que usamos para crearlo
        assert producto.nomre == 'Producto de prueba'


    def test_geId_producto_succesfully(self):
        """
         vamos a validar que el método traiga la informacion de un producto por id

        """
        create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        codigo_pro = 'PRU-23423'
        producto = get_producto(codigo_pro)
        assert producto.codigo == 'PRU-23423'

    def test_update_producto_succesfully(self):
        """
         vamos a validar que el método cambie de precio segun codigo del producto

        """
        create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        codigo_pro = 'PRU-23423'
        
        update_precio_producto('Producto de prueba','PRU-23423','15000' )
        producto = get_producto(codigo_pro)
        assert producto.precio == 15000


    def test_delete_producto_succesfully(self):
        """
         vamos a validar que el método elimine segun el producto

        """
        producto = create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        
        delete_producto(producto)
        # Validamos que el usuario ya no exista dentro de nuestra base de datos de prueba
        with pytest.raises(producto.DoesNotExist):
            get_producto(producto.id)
        

    
       
