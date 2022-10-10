Proyecto final Python: Blog colaborativo de cine

La idea de la pagina es que los usuarios puedan registrarse crendo una sesion con pocos requisitos y puedan subir reseñas de peliculas para que otros usuarios que ingresan al sitio puedan elegir una pelicula para ver.

Contamos con la AppProyecto donde estan los models y views para la creacion de peliculas, y la AppUser con todo lo relacionado al registro e inicio de sesion de los usuarios al sistema.

Pruebas:

1. Con el boton de registrarse en la nav_bar nos lleva a un formulario de registro de usuario.
2. Luego con el usuario creado podemos iniciar sesion con los datos anteriormente ingresados.
3. Con la siguiente url http://127.0.0.1:8000/UserProyecto/avatar/ podemos agregarle un avatar a nuestro usuario.
4. Luego con la url http://127.0.0.1:8000/UserProyecto/editar/ nos permitira editar los datos del usuario (solo si estamos dentro de la sesion)
5. Con el boton "Cerrar sesion" se cierra sesion ingresada y se retorna al inicio.
6. En el apartado de peliculas (siempre y cuando estemos con la sesion iniciada) se llega a un formulario para agregar peliculas nuevas.
7. Con la url http://127.0.0.1:8000/AppProyecto/pelicula_buscar/ (siempre y cuando estemos con la sesion iniciada) vamos a acceder a un formulario que nos va a permitir buscar peliculas por su nombre. Una vez que introducimos el nombre le damos "buscar" y nos va a llevar a una pagina con los detalles encontrados.

La idea es continuar desarrollando el sitio dandole mas opciones y mejorar la calidad del diseño que por cuestiones de tiempo se dejo con la base del bootstrap.

Enlace al video de funcionalidad:  https://youtu.be/7b6eZF8VDXQ

