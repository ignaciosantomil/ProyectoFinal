from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime
from django.core.exceptions import MultipleObjectsReturned
from AppProyecto.forms import *


def inicio(request):
    return render(request, 'index.html')


def pelicula(request):
    peliculas = Pelicula.objects.all()[:3]
    contexto = {
        'peliculas': peliculas
    }

    return render(request, 'AppProyecto/pelicula.html', contexto)


def pelicula_form(request):
    if request.method == 'POST':
        mi_formulario = PeliculaForm(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            pelicula1 = Pelicula(nombre=data.get('nombre'), director=data.get('director'), anio=data.get('año'), genero=data.get('genero'), descripcion=data.get('descripcion'))
            pelicula1.save()

            return redirect('AppProyectoInicio')

    contexto = {
        'form': PeliculaForm
    }

    return render(request, 'AppProyecto/pelicula.html', contexto)

def pelicula_buscar(request):
    contexto = {
        'form': PeliculaBuscar(),
    }
    return render(request, 'AppProyecto/pelicula_buscar.html', contexto)


def pelicula_buscar_post(request):
    nombre = request.GET.get('nombre')

    peliculas = Pelicula.objects.filter(nombre__icontains=nombre)

    contexto = {
        'peliculas': pelicula

    }
    return render(request, 'AppProyecto/pelicula_filtrado.html', contexto)

def pelicula_editar(request, nombre):
    editar = Pelicula.objects.get(nombre=nombre)

    if request.method == 'POST':
        mi_formulario = PeliculaForm(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            editar.nombre = data.get('nombre')
            editar.director = data.get('director')
            editar.anio = data.get('anio')
            editar.genero = data.get('genero')
            editar.descripcion = data.get('descripcion')

            editar.save()

            return redirect('AppProyectoInicio')

    contexto = {
        'form': PeliculaForm(
            initial={
                'nombre': editar.nombre,
                'director': editar.director,
                'anio': editar.anio,
                'genero': editar.genero,
                'descripcion': editar.descripcion,

            })
    }

    return render(request, 'AppProyecto/pelicula_form.html', contexto)
