from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path('', inicio, name='AppProyectoInicio'),
    path('peliculas/', pelicula, name='AppProyectoPeliculas'),
    path('pelicula_buscar/', pelicula_buscar, name='AppProyectoPeliculaBuscar'),
    path('pelicula_buscar_post/', pelicula_buscar_post, name='AppProyectoPeliculaBuscarPost'),
    path('pelicula_form/', pelicula_form, name='AppProyectoPeliculaForm'),
    path('about/', about, name='AppProyectoAbout'),
]
