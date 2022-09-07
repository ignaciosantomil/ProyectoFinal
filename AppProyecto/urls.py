from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path('', inicio, name='AppProyectoInicio'),
    path('registro/', cliente, name='AppProyectoClientes'),
    path('cliente_form/', cliente_form, name= 'AppProyectoClienteForm'),
    path('cliente_buscar/', cliente_buscar, name= 'AppProyectoClienteBuscar'),
    path('cliente_buscar_post/', cliente_buscar_post, name= 'AppProyectoClienteBuscarPost'),

]
