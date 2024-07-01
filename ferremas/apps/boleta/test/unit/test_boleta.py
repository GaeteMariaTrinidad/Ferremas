import pytest
from views import create_boleta, get_boleta, update_boleta, delete_boleta
from datetime import datetime

@pytest.mark.django_db
class TestBoletaService:
    def test_create_boleta_successfully(self):
        """
        Validamos que el método crear boleta funcione correctamente
        """
        boleta = create_boleta(1000, datetime.now(), 'Benjamin Morales', 'Taladro percutor Bauker, Caja tornillos', 1)
        
        
        assert boleta.cliente == 'Benjamin Morales'

    def test_get_boleta_successfully(self):
        """
        Validamos que el método traiga la información de una boleta por número de boleta
        """
        create_boleta(1000, datetime.now(), 'Benjamin Morales', 'Taladro percutor Bauker, Caja tornillos', 1)
        boleta = get_boleta(1)
        assert boleta.numBoleta == 1

    def test_update_boleta_successfully(self):
        """
        Validamos que el método actualice los campos de una boleta según el número de boleta
        """
        create_boleta(1000, datetime.now(), 'Benjamin Morales', 'Taladro percutor Bauker, Caja tornillos', 1)
        
        update_boleta(1, total=2000, cliente='Maria Gaete')
        boleta = get_boleta(1)

        assert boleta.total == 2000
        assert boleta.cliente == 'Maria Gaete'

    def test_delete_boleta_successfully(self):
        """
        Validamos que el método elimine una boleta según el número de boleta
        """
        boleta = create_boleta(1000, datetime.now(), 'Benjamin Morales', 'Taladro percutor Bauker, Caja tornillos', 1)
        
        delete_boleta(boleta)
        
        assert get_boleta(1) is None
