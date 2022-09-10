from django.db import models
from django.shortcuts import render


class Producto(models.Model):
    modelo = models.CharField(max_length=30)
    precio = models.FloatField()


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
