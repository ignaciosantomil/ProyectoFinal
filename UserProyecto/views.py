from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserProyecto.forms import UserRegisterForm


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:

                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio')

            else:
                messages.info(request, 'Verificar usuario y/o contraseña')
        else:

            messages.info(request, 'Inicio de sesion fallido!')

        return redirect('AppProyectoInicio')

    contexto = {
        'form': AuthenticationForm(),
        'nombre_form': 'Login'
    }

    return render(request, 'UserProyecto/login.html', contexto)


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue creado correctamente!')

        else:
            messages.info(request, 'Tu usuario no pudo ser registrado')

        return redirect('AppProyectoInicio')

    contexto = {
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
        }

    return render(request, 'UserProyecto/login.html', contexto)

