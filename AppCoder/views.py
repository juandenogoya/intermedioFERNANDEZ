from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def cursos (request):
    return render (request, 'AppCoder/cursos.html')

def estudiantes (request):
    return render (request, 'AppCoder/estudiantes.html')

def profesores (request):
    return render (request, 'AppCoder/profesores.html')

def entregables (request):
    return render (request, 'AppCoder/entregables.html')

def inicio (request):
    return render (request, 'AppCoder/inicio.html')

