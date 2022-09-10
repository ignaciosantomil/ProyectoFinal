from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path('', inicio, name='AppProyectoInicio'),
    path('cliente/', cliente, name='AppProyectoClientes'),
    path('cliente_form/', cliente_form, name= 'AppProyectoClienteForm'),
    path('cliente_buscar/', cliente_buscar, name= 'AppProyectoClienteBuscar'),
    path('cliente_buscar_post/', cliente_buscar_post, name= 'AppProyectoClienteBuscarPost'),
    path('cliente_eliminar/<int:dni>', cliente_eliminar, name='AppProyectoClienteEliminar'),
    path('editar_cliente/<int:dni>', cliente_editar, name='AppProyectoClienteEditar'),
]
