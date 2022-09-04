from django.shortcuts import render, redirect
from .models import *


def inicio(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
