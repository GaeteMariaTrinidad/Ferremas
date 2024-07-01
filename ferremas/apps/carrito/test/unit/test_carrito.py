import pytest
from apps.producto.models import Producto
from apps.usuario.models import Usuario
from apps.carrito.models import Carrito

@pytest.mark.django_db
def test_carrito_creation():
    usuario = Usuario.objects.create(nombre='Usuario', apellido='Prueba', contrasena='12345', correo='correo@correo.com', edad=29)
    producto = Producto.objects.create(nomre='Producto Prueba', marca='Bauker', stock=5, codigo='001', precio=4990)

    carrito = Carrito.objects.create(usuario=usuario, producto=producto, cantidad=2)

    assert carrito.id is not None
    assert carrito.usuario == usuario
    assert carrito.producto == producto
    assert carrito.cantidad == 2

   
    expected_str = f"{usuario.nombre} - {carrito.cantidad} - {producto.nomre} - {carrito.id} - {producto.precio}"
    assert str(carrito) == expected_str

@pytest.mark.django_db
def test_carrito_get():
    usuario = Usuario.objects.create(nombre='Usuario', apellido='Prueba', contrasena='12345', correo='correo@correo.com', edad=29)
    producto = Producto.objects.create(nomre='Producto Prueba', marca='Bauker', stock=5, codigo='001', precio=4990)

    carrito = Carrito.objects.create(usuario=usuario, producto=producto, cantidad=2)

  
    carrito_from_db = Carrito.objects.get(id=carrito.id)
    assert carrito_from_db == carrito

@pytest.mark.django_db
def test_carrito_update():
    usuario = Usuario.objects.create(nombre='Usuario', apellido='Prueba', contrasena='12345', correo='correo@correo.com', edad=29)
    producto = Producto.objects.create(nomre='Producto Prueba', marca='Bauker', stock=5, codigo='001', precio=4990)

    carrito = Carrito.objects.create(usuario=usuario, producto=producto, cantidad=2)


    carrito.cantidad = 5
    carrito.save()

   
    carrito_from_db = Carrito.objects.get(id=carrito.id)
    assert carrito_from_db.cantidad == 5

@pytest.mark.django_db
def test_carrito_delete():
    usuario = Usuario.objects.create(nombre='Usuario', apellido='Prueba', contrasena='12345', correo='correo@correo.com', edad=29)
    producto = Producto.objects.create(nomre='Producto Prueba', marca='Bauker', stock=5, codigo='001', precio=4990)

    carrito = Carrito.objects.create(usuario=usuario, producto=producto, cantidad=2)

    
    carrito_id = carrito.id
    carrito.delete()

    with pytest.raises(Carrito.DoesNotExist):
        Carrito.objects.get(id=carrito_id)
