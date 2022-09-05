from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import datetime
from django.core.exceptions import MultipleObjectsReturned


def inicio(request):
    return render(request, 'index.html')


def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes
    }

    return render(request, 'AppProyecto/registro.html', contexto)


