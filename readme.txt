https://we.tl/t-hiWnZkUfK5 ----> Link Video

Este proyecto es una aplicación web desarrollada con el framework Django. Proporciona una interfaz para gestionar productos, vendedores, compradores y devoluciones.

Requisitos:
    Python 3.9+
    Django 4.0+
    Base de datos SQLite (configuración por defecto de Django)

Instalacion Django:
    pip install django
    
Instalacion Pillow:
    pip install Pillow

Crear un entorno virtual:
    python -m venv venv
    venv\Scripts\activate

Configura la base de datos:
    python manage.py migrate

Inicia el servidor de desarrollo:
    python manage.py runserver

Acceder a la aplicación en tu navegador: 
    http://127.0.0.1:8000/

Archivos Principales:
    views.py: Contiene las funciones que gestionan las vistas de la aplicación.
    urls.py: Define las rutas URL y las asocia con las vistas correspondientes.
    models.py: Define las clases de modelos (Productos, Vendedor, Comprador, Devolución) que representan las tablas de la base de datos.

Modelos
    Productos
        producto: Nombre del producto (cadena, máximo 30 caracteres).
        unidades: Número de unidades disponibles (entero).
        precio: Precio del producto (entero).

    Comprador
        nombre: Nombre del comprador (cadena, máximo 30 caracteres).
        apellido: Apellido del comprador (cadena, máximo 30 caracteres).
        email: Correo electrónico del comprador.

    Vendedor
        nombre: Nombre del vendedor (cadena, máximo 30 caracteres).
        apellido: Apellido del vendedor (cadena, máximo 30 caracteres).
        email: Correo electrónico del vendedor.
        codigo: Código único del vendedor (cadena, máximo 50 caracteres).

    Devolución
        producto: Nombre del producto devuelto (cadena, máximo 100 caracteres).
        fechaDeEntrega: Fecha de devolución.
        devuelto: Estado de la devolución (booleano).

    Profile 
        user: Cada perfil está vinculado a un único usuario a través de una relación uno a uno.
        photo: Permite cargar una imagen para el perfil de usuario.

Configuración Adicional
    Templates
        Los templates se encuentran en el directorio templates/WebApp/. Puedes personalizar las vistas modificando estos archivos HTML:
        index.html
        productos.html
        vendedores.html
        compradores.html
        devoluciones.html

    Estilos
        Para agregar estilos, coloca los archivos CSS en el directorio static/WebApp/css/ y enlázalos en los templates HTML.
