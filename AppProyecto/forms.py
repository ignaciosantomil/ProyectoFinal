from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    nacimiento = forms.DateField()
    mail = forms.EmailField()
    dni = forms.IntegerField()


class ClienteBuscar(forms.Form):
    dni = forms.IntegerField()
