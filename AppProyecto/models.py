from django.db import models
from django.shortcuts import render
class Producto(models.Model):
    modelo = models.CharField(max_length=30)
    precio = models.FloatField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    mail = models.EmailField()
