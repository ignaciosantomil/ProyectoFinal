from django.urls import path
from AppProyecto.views import *

urlpatterns = [
    path('', inicio),
    path('registro/', cliente, name='clientes')

]
