# Documentación APIs  
### En este documento podrá encontrar los endpoints existentes en el proyecto y sus instrucciones de ejecución.
#
## Endpoint 1: Mostrar los productos del carrito
- URL: `/api/carrito_list`
- Método HTTP: GET
- Parámetros: Ninguno
- Estructura necesaria: No requiere
- Esperable respuesta carrito con productos:
```bash
{
    "message": "Success",
    "Articulos del Carrito ": [
        {
            "id": 1,
            "nombre": "Taladro Percutor Bosch",
            "cantidad": 4,
            "precio": 20000
        },
        {
            "id": 2,
            "nombre": "Taladro Percutor Makita",
            "cantidad": 3,
            "precio": 25000
        },
        {
            "total": 155000,
            "id_carrito": 1
        }
    ]
}
```
- Esperable respuesta carrito vacío:
```bash
{
    "message": "El Carrito está vacío"
}
```

## Endpoint 2: Agregar un producto al carrito

- URL: `/api/carrito_add`
- Método HTTP: POST
- Parámetros: 
```bash
- "id": (int, requerido): ID de la herramienta a agregar
- "cantidad" (int, requerido): Cantidad del producto a agregar
```
- Estructura necesaria:
```bash
{
    "id": 2,
    "cantidad": 1
}
```
- Esperable respuesta producto agregado:
```bash
{
    "message":"El producto se ha gregado al carrito"
}
```

## Endpoint 3: Eliminar un carrito

- URL: `/api/carrito_delete/<int:id>/`
- Método HTTP: DELETE
- Parámetros: 
```bash
- "id": (int, requerido): ID del carrito a eliminar
```
- Estructura necesaria: No requiere
- Esperable respuesta carrito eliminado:

```bash
{
    'message':"Success",'El carrito se ha eliminado: ':carritos_delete
}
```
- Esperable respuesta carrito no encontrado:

```bash
{
    "message": "El carrito no se ha encontrado"
}
```