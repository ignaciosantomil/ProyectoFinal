from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    nacimiento = forms.DateField()
    mail = forms.EmailField()
    dni = forms.IntegerField()


class PeliculaForm(forms.Form):
    pelicula = forms.CharField(max_length=40)
    director = forms.CharField(max_length=30)
    anio = forms.IntegerField
    genero = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=140)


class ClienteBuscar(forms.Form):
    nombre = forms.CharField(max_length=30)
