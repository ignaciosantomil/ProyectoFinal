from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime
from django.core.exceptions import MultipleObjectsReturned
from AppProyecto.forms import *


def inicio(request):
    return render(request, 'index.html')


def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes
    }

    return render(request, 'AppProyecto/cliente.html', contexto)


def cliente_form(request):
    if request.method == 'POST':
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            cliente1 = Cliente(nombre=data.get('nombre'), nacimiento=data.get('nacimiento'), mail=data.get('mail'), dni=data.get('dni'))
            cliente1.save()

            return redirect('AppProyectoInicio')

    contexto = {
        'form': ClienteForm
    }

    return render(request, 'AppProyecto/cliente_form.html', contexto)

def pelicula_form(request):
    if request.method == 'POST':
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            pelicula1 = Pelicula(nombre=data.get('nombre'), director=data.get('director'), anio=data.get('anio'), genero=data.get('genero'), descripcion=data.get('descripcion'))
            pelicula1.save()

            return redirect('AppProyectoInicio')

    contexto = {
        'form': PeliculaForm
    }

    return render(request, 'AppProyecto/pelicula_form.html', contexto)

def cliente_buscar(request):
    contexto = {
        'form': ClienteBuscar(),
    }
    return render(request, 'AppProyecto/cliente_buscar.html', contexto)


def cliente_buscar_post(request):
    nombre = request.GET.get('nombre')

    clientes = Cliente.objects.filter(nombre__icontains=nombre)

    contexto = {
        'clientes': clientes

    }
    return render(request, 'AppProyecto/cliente_filtrado.html', contexto)


def cliente_eliminar(request, nombre):
    eliminar_cliente = Cliente.objects.get(nombre=nombre)
    eliminar_cliente.delete()

    messages.info(request, f'El cliente de dni: {eliminar_cliente} fue eliminado satisfactoriamente')

    return redirect('AppProyectoInicio')


def cliente_editar(request, nombre):
    editar = Cliente.objects.get(nombre=nombre)

    if request.method == 'POST':
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            editar.nombre = data.get('nombre')
            editar.nacimiento = data.get('nacimiento')
            editar.mail = data.get('mail')
            editar.dni = data.get('dni')

            editar.save()

            return redirect('AppProyectoInicio')

    contexto = {
        'form': ClienteForm(
            initial={
                'nombre': editar.nombre,
                'dni': editar.dni

            })
    }

    return render(request, 'AppProyecto/cliente_form.html', contexto)
