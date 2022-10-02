from django import forms


class PeliculaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    director = forms.CharField(max_length=30)
    anio = forms.IntegerField
    genero = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=140)


class PeliculaBuscar(forms.Form):
    nombre = forms.CharField(max_length=30)
