Proyecto final Python: Blog colaborativo de cine

La idea de la pagina es que los usuarios puedan registrarse crendo una sesion con pocos requisitos y puedan subir reseñas de peliculas para que otros usuarios que ingresan al sitio puedan elegir una pelicula para ver.

Contamos con la AppProyecto donde estan los models y views para la creacion de peliculas, y la AppUser con todo lo relacionado al registro e inicio de sesion de los usuarios al sistema.

Pruebas:

1. Con el boton de registrarse en la nav_bar nos lleva a un formulario de registro de usuario.
2. Luego con el usuario creado podemos iniciar sesion con los datos anteriormente ingresados.
3. Con la siguiente url http://127.0.0.1:8000/UserProyecto/avatar/ podemos agregarle un avatar a nuestro usuario.
4. Luego con la url http://127.0.0.1:8000/UserProyecto/editar/ nos permitira editar los datos del usuario (solo si estamos dentro de la sesion)
5. Con el boton "Cerrar sesion" se cierra sesion ingresada y se retorna al inicio.
6. En el apartado de peliculas se llega a un formulario para agregar peliculas nuevas.

La idea es continuar desarrollando el sitio dandole mas opciones y mejorar la calidad del diseño que por cuestiones de tiempo se dejo con la base del bootstrap.


