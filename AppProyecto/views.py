from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime
from django.core.exceptions import MultipleObjectsReturned
from AppProyecto.forms import ClienteForm, ClienteBuscar


def inicio(request):
    return render(request, 'index.html')


def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes
    }

    return render(request, 'AppProyecto/registro.html', contexto)


def cliente_form(request):
    if request.method == 'POST':
        mi_formulario = ClienteForm(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            cliente1 = Cliente(nombre=data.get('nombre'), nacimiento=data.get('nacimiento'), mail=data.get('mail'))
            cliente1.save()

            return redirect('AppProyectoInicio')

    contexto = {
        'form': ClienteForm
    }

    return render(request, 'AppProyecto/cliente_form.html', contexto)


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
