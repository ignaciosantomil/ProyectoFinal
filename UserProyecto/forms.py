from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from UserProyecto.models import Avatar


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar

        fields = '__all__'
