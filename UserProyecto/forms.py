from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserProyecto.models import Avatar


class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    nacimiento = forms.DateField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'nacimiento', 'email',)



class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar

        fields = '__all__'


