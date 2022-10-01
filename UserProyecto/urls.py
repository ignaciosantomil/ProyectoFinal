from django.contrib.auth.views import LogoutView
from django.urls import path

from UserProyecto.views import *

urlpatterns = [
    path('login/', login_request, name='UserProyectoLogin'),
    path('registro/', register, name='UserProyectoRegister'),
    path('logout/', LogoutView.as_view(template_name='UserProyecto/logout.html'), name='UserProyectoLogout'),


]
