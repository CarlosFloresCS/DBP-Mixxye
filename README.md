# Mixxye :notes:

¿Recuerdas los reproductores de MP3? ¿ O tal vez las músicas que grababas en el celular? :iphone:
En pocas cuentas, ambos dispositivos sirvieron como una biblioteca de música portatil.
**Mixxye** ofrece el mismo servicio pero de manera actualizada. Esta plataforma permite crear una cuenta, con usuario y contraseña, para poder crear, guardar, editar y personalizar la variedad de listas musicales que quieras a traves del link de tus canciones favoritas :smile: :headphones:

## Objetivos :white_check_mark:

- Objetivo general
    - Crear una página web / plataforma capaz de interactuar con el usuario y conectarse a un servidor y una base de datos
- Objetivos especificos
    - Implementar una interfaz deductiva, amigable e interactiva
    - Crear un modelo adecuado para guardar listas musicales
    - Implementar el concepto de CRUD para el modelo principal de la página web

## Mision :dart:

Brindar un espacio de almacenamiento musical a nuestros usuarios para que puedan deleitarse con sus canciones favoritas del ayer, hoy y siempre.

## Vision :eye:

Conectar recuerdos con canciones para atesorar los momentoes mas memorables junto a nuestros usuarios 

## Tecnologias empleadas en Front-end, Back-end y Database :top:

### Front-end 

- HTML <>
    
    Sistema de etiquetas que describen el contenido de la pagina web. Está conformada por bloques según el tipo de contenido que se implemente.

- CSS

    Representación visual del HTML. Proporciona diseño y estilo a los bloques implementados en HTML.

### Back-end

- Python

    Lenguaje de programacion que permite implementar las acciones de la pagina web en el servidor gracias a sus librerias. Las lineas de codigo desarrolladas reciben y procesan informacion del cliente, y elaboran y ejecutan una respuesta desde el servidor. Asimismo, intercambia informacion con la base de datos.

- Flask

    Framework que facilita la implementacion de las acciones en el servidor a traves de plantillas y librerias. 

### Base de datos

- SQLAlchemy

    Conjunto de herramientas que trabaja directamente con la base de datos. Es capaz de almacenar, modificar y extraer informacion de esta. Este conjunto de herramientas en concreto trabaja exclusivamente con python, pues convierte objetos de este lenguaje en tablas que se integran a la base de datos. 

## Script principal:      :briefcase:

El script principal es el archivo con nombre [Mixxye.py](https://github.com/CarlosFloresCS/DBP-Mixxye/blob/main/aplicacion/Mixxye.py)

## Host :business_suit_levitating:

El proyecto emplea un host local ya que trabaja con la base de datos PostgreSQL. Este host se identifica con un numero de [IP](http://127.0.0.1:3000/) y es el mismo para las versiones del proyecto instaladas en diferentes computadoras.

## Forma de autenticacion :mag:

La autenticación se realizó gracias a la librería 'werkzeug' y sus 'import generate_password_hask' y 'check_password_hash', donde el primero genera la encriptación y el segundo comprueba si el valor cifrado coincide con el valor original.

## Manejo de errores 

- Redireccion (300 - 308)

    Se muestra el mensaje por defecto del navegador que usa el usuario.

- Errores de cliente (400 - 451)

    Se muestra el mensaje por defecto del navegador que usa el usuario. Asimismo, se hace enfasis en la gestion de la memoria cache y las cookkies. Ademas, alguno de estos errores muestran un mensaje personalizado pidiendo al usuario que reingrese la solicitud.

- Errores de servidor (500 - 511)

    Se muestra el mensaje por defecto del navegador que usa el usuario.

## Request y responses :inbox_tray: | :outbox_tray: 

- Registro

    La solicitud del usuario es el registro de una cuenta en la plataforma. La respuesta de la misma es el redireccionamiento a un formulario para consignar los datos. Después de ser enviados por el usuario, muestra la página de inicio del perfil de la nueva cuenta.

- Inicio de sesion

    La solicitud del usuario es el logeo en la plataforma. La respuesta de la misma es el redireccionamiento a un formulario para consignar los datos de inicio de sesión. Después de ser enviados por el usuario, muestra la página de inicio del perfil de la nueva cuenta.

- Registro de playlist

    La solicitud del usuario inicia al entrar a la pagina de inicio de su perfil. En la parte superior izquierda, encuentra dos campos para registrar una cancion en su playlist, mediante el nombre y link de esta. El boton de *save* retorna como respuesta la visualizacion de la cancion agregada en la sección de *Mi biblioteca*.

- Eliminación de una canción

    La solicitud del usuario es presionar el boton *delete* que se encuentra al lado derecho de la canción seleccionada en la sección *Mi biblioteca*. La respuesta de la página es quitar la canción de la lista del usuario asi como de la base de datos.

## Ejecución del sistema (Scripts) :card_index_dividers:

Uno de los primeros archivos a ejecutar es aquel que contiene el [entorno virtual](https://github.com/CarlosFloresCS/DBP-Mixxye/tree/main/venv). Luego de este, se ejecuta el [cuerpo](https://github.com/CarlosFloresCS/DBP-Mixxye/tree/main/aplicacion) de la plataforma. En este ultimo se encuentra script principal es el archivo con nombre [Mixxye.py](https://github.com/CarlosFloresCS/DBP-Mixxye/blob/main/aplicacion/Mixxye.py).

## Integrantes :man_technologist:

- Alexandra Amy Zevallos Carhuamaca 
- Alexis Raza Estrada
- Carlos Alonso Flores Panduro
- Fernando Adriano Choqque Mejia 
