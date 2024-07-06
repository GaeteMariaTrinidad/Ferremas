import pytest
from apps.mermaProducto.views import create_mermaProducto, get_mermaProducto, delete_mermaProducto, update_mermaProducto
from apps.producto.views import create_producto
from datetime import datetime

@pytest.mark.django_db
class TestMermaProductoService:
    def test_create_mermaProducto_successfully(self):
        """
        Validamos que el método crear merma producto funcione correctamente
        """
        prod = create_producto('Producto de prueba', 'Mprueba', '1', 'PRU-23423', '10000')
        mermaProducto = create_mermaProducto(prod, '15', datetime.now(), 5000)


        assert mermaProducto.detalle_merma == '15'

    def test_get_mermaProducto_successfully(self):
        """
        Validamos que el método obtenga la información de una merma por su detalle
        """
        prod = create_producto('Producto de prueba2', 'Mprueba2', '2', 'PRU-234232', '10000')
        create_mermaProducto(prod, '25', datetime.now(), 5000)
        mermaProducto = get_mermaProducto('25')
        assert mermaProducto.detalle_merma == '25'

    def test_delete_mermaProducto_successfully(self):
        """
        Validamos que el método elimine una merma producto segun el numero del detalle
        """
        print("1")
        prod = create_producto('Producto de prueba3', 'Mprueba3', '3', 'PRU-234233', '10000')
        print("2")
        mermaProducto = create_mermaProducto(prod, '55', datetime.now(), 5000)
        print("3")

        delete_mermaProducto(mermaProducto)
        print("4")
        assert get_mermaProducto('55') is None 

    def test_update_mermaProducto_successfully(self):
        """
        Validamos que el método actualice los campos del detalle de una merma producto
        """
        prod = create_producto('Producto de prueba3', 'Mprueba3', '3', 'PRU-234233', '10000')
        create_mermaProducto(prod, '15', datetime.now(), 5000)
        
        update_mermaProducto('15',valorPerdida = 2555,)
        mermaProducto = get_mermaProducto('15')

        assert mermaProducto.valorPerdida == 2555
        

        


