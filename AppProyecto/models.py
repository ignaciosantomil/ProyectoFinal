from django.db import models
from django.shortcuts import render


class Pelicula(models.Model):
    pelicula = models.CharField(max_length=40)
    director = models.CharField(max_length=30)
    anio = models.IntegerField
    genero = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=140)


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    mail = models.EmailField()
    dni = models.IntegerField(unique=True)

    def __str__(self):
        return f"Cliente: {self.nombre}"


class servicio_cliente(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    consulta = models.CharField(max_length=140)
