# Guía de configuración y ejecución de pruebas del proyecto FERREMAS 

## Requisitos previos
- Python 3.10.7
- pip
- virtualenv
- Django
- Postman
- pytest
- Visual Studio Code 

## 1. Crear y activar el ambiente virtual

### Paso 1: Instalar virtualenv
En caso de no tener instalado virtualenv, puedes instalarlo desde la termina con el siguiente comando:
```bash
pip install virtualenv
```

### Paso 2: Entrar en la carpeta del proyecto  `ferremas`

```bash
cd .\ferremas\
```


### Paso 3: Crear ambiente virtual
Ir a la carpeta raíz del proyecto crear el ambiente virtual desde la terminal:
```bash
python -m virtualenv venv
```
Al ejecutarlo, se agregará una nueva carpeta llamada `venv`.

### Paso 4: Activar ambiente virtual
Activamos el ambiente virtual con el comando:
```bash
.\venv\Scripts\activate
```

### Paso 5: Instalar paquetes necesarios para el funcionamiento de las APIs
Dentro del proyecto se encuentra un archivo llamado "requirements.txt", el cual contiene el detalle de las dependencias necesarias para su correcto funcionamiento. Ejecute el siguiente comando:
```bash
pip install -r requirements.txt
```

### Paso 6: Verificación de dependencias instaladas:
Para asegurarse de que los archivos instalados sean los que se requieren, ejecute:
```bash
pip list
```

### Paso 7: Ejecutar servidor Django:

Para levantar el servidor y comprobar que funciona correctamente, ejecutamos el siguiente comando:
```bash
python manage.py runserver
```


## 2. Ejecución de las pruebas con Pytest 

### Paso 1: Ejecutar pruebas unitarias y de integración:
Para realizar las pruebas, se debe verificar que el archivo `pytest.ini` exista en el directorio `venv` y esté escrito correctamente: 
```bash
[pytest]
DJANGO_SETTINGS_MODULE = ferremas.settings
python_files = test.py test_*.py *_tests.py
```

Para ejecutar todas las pruebas, se debe escribir el siguiente comando:

```bash
pytest -v
```
#

## Con estas instrucciones podrá ejecutar correctamente el proyecto, sus pruebas unitarias y de integración. 





