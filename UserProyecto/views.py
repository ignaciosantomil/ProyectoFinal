from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserProyecto.forms import UserRegisterForm, AvatarForm
from UserProyecto.models import Avatar


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


@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':

        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.first_name = data.get('first_name')
            usuario.last_name = data.get('last_name')
            usuario.email = data.get('email')

            usuario.save()

            messages.info(request, 'Tu usuario fue editado correctamente!')

        else:
            messages.info(request, 'Tu usuario no pudo ser editado')

        return redirect('AppProyectoInicio')

    contexto = {
        'form': UserRegisterForm(
            initial={
                'username': usuario.username,
                'first_name': usuario.first_name,
                'last_name': usuario.last_name,
                'email': usuario.email,
            }),
        'nombre_form': 'Registro'
    }

    return render(request, 'UserProyecto/login.html', contexto)


def upload_avatar(request):
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get('usuario'))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data['imagen']
                avatar.save()

            else:
                avatar = Avatar(user=data.get('user'), imagen=data.get('imagen'))
                avatar.save()
        return redirect('AppProyectoInicio')

    contexto = {
        'form': AvatarForm(),
        'nombre_form': 'Avatar form'

    }
    return render(request, 'UserProyecto/avatar.html', contexto)
