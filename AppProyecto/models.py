from django.db import models
from django.shortcuts import render


class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    director = models.CharField(max_length=30)
    anio = models.IntegerField
    genero = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=140)


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"Usuario: {self.nombre}"

