from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppCoder.forms import *

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

def familiar (request): #todos son paramatros, un pedido (request), un template y un diccionario siempre.
    return render (request, 'AppCoder/familia.html', {}) 

def futbol (request):
    return render (request, "AppCoder/futbol.html")



""" def cursoFormulario (request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        comision = request.POST["comision"]
        curso = Curso (nombre= nombre, comision = comision) 
        curso.save()
        return render (request, "AppCoder/inicio.html", {"mensaje": "Curso Guardado Correctamente"})


        pass
    else:
        return render (request, 'AppCoder/cursoFormulario.html') """



#VISTA "BASICA De CREACION DE FORMULARIOS"
def cursoFormulario (request):
    if request.method == "POST":
        form = CursoForm (request.POST)
        if form.is_valid():
            informacion = form.cleaned_data #ayuda a ver mejor la informacion, conviernte en un diccionario.
            nombre = informacion ["nombre"]
            comision = informacion ["comision"]
            curso = Curso (nombre = nombre, comision = comision)
            curso.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Curso Guardado Correctamente"})
        else:
            return render (request, "AppCoder/cursoFormulario.html", {"form": form, "mensaje": "Informacion Invalida"})

    else:
        formulario = CursoForm()
        return render (request, "AppCoder/cursoFormulario.html", {"form": formulario})



def profeFormulario (request):
    if request.method == "POST":
        form = ProfeForm (request.POST)
        if form.is_valid():
            informacion = form.cleaned_data #ayuda a ver mejor la informacion, conviernte en un diccionario.
            nombre = informacion ["nombre"]
            apellido = informacion ["apellido"]
            email = informacion ["email"]
            profesion = informacion ["profesion"]

            profesor = Profesor (nombre = nombre, apellido = apellido, email = email, profesion = profesion)
            profesor.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Profesor Guardado Correctamente"})
        else:
            return render (request, "AppCoder/profeFormulario.html", {"form": form, "mensaje": "Informacion Invalida"})

    else:
        formulario = ProfeForm()
        return render (request, "AppCoder/profeFormulario.html", {"form": formulario})

#CREACION DE CONTROLADOR de FUTBOL
def futbolFormulario (request):
    if request.method == "POST":
        form = FutbolForm (request.POST)
        if form.is_valid():
            informacion = form.cleaned_data #ayuda a ver mejor la informacion, conviernte en un diccionario.
            nombre = informacion ["nombre"]
            apellido = informacion ["apellido"]
            anio_nacimiento = informacion ["anio_nacimiento"]
            futbol = Futbol (nombre = nombre, apellido = apellido, anio_nacimiento = anio_nacimiento)
            futbol.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Jugador Guardado Correctamente"})
        else:
            return render (request, "AppCoder/futbolFormulario.html", {"form": form, "mensaje": "Informacion Invalida"})

    else:
        formulario = FutbolForm()
        return render (request, "AppCoder/futbolFormulario.html", {"form": formulario})


#CREACION CONTROLADOR FAMILIAR
def familiaFormulario (request):
    if request.method == "POST":
        form = FamiliaForm (request.POST)
        if form.is_valid():
            informacion = form.cleaned_data #ayuda a ver mejor la informacion, conviernte en un diccionario.
            nombre = informacion ["nombre"]
            apellido = informacion ["apellido"]
            fecha_nacimiento = informacion ["fecha_nacimiento"]
            familiar = Familiar (nombre = nombre, apellido = apellido, fecha_nacimiento = fecha_nacimiento)
            familiar.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Familiar Guardado Correctamente"})
        else:
            return render (request, "AppCoder/familiaFormulario.html", {"form": form, "mensaje": "Informacion Invalida"})

    else:
        formulario = FamiliaForm()
        return render (request, "AppCoder/familiaFormulario.html", {"form": formulario})



#CREAR un VISTA que me permita ver en una lista las personas creadas
def leerPersonas (request):
    personas = Persona.objects.all() #Es "all" porque quiero ver todas las personas.
    return render (request, "AppCoder/personas.html", {"personas": personas})




def agregarPersona (request):
    if request.method == "POST":
        formulario = PersonaForms(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nombre = info["nombre"]
            apellido = info ["apellido"]
            email = info ["email"]
            fecha_nacimiento = info ["fechaNacimiento"]
            tieneObraSocial = info ["tieneObraSocial"]
            persona = Persona (nombre = nombre, apellido = apellido, fechaNacimiento = fecha_nacimiento, tieneObraSocial = tieneObraSocial)
            persona.save()

            persona = Persona.objects.all()
            return render (request, "AppCoder/personas.html", {"personas": persona, "mensaje": "Persona Guardada Correctamente"})

        
        else:
            return render(request, "AppCoder/agregarPersona.html", {"formulario": formulario, "mensaje": "Informacion No Valida"})
    else:
        form = PersonaForms()
        return render(request, "AppCoder/agregarPersona.html", {"form": form})



#VISTA PARA AGREGAR PERSONAS
def editarPersona (request, id):
    persona = Persona.objects.get(id=id)
    if request.method == "POST":
        formulario = PersonaForms(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nombre = info ["nombre"]
            apellido = info ["apellido"]
            email = info ["email"]
            fecha_nacimiento = info ["fechaNacimiento"]
            tieneObraSocial = info ["tieneObraSocial"]
            persona.nombre = nombre
            persona.apellido = apellido
            persona.email = email
            persona.fechaNacimiento = fecha_nacimiento
            persona.tieneObraSocial = tieneObraSocial

            persona.save()
            persona = Persona.objects.all()
            return render (request, "AppCoder/personas.html", {"personas": persona, "mensaje": "Persona Editada Correctamente"})


    else: 
   
        form = PersonaForms (initial = {"nombre": persona.nombre, "apellido": persona.apellido, "email": persona.email, "fecha_nacimiento": persona.fechaNacimiento, "tieneObraSocial": persona.tieneObraSocial})
        return render (request, "AppCoder/editarPersona.html", {"formulario": form, "personas": persona})
    

def eliminarPersona (request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    persona = Persona.objects.all()
    return render (request, "AppCoder/personas.html", {"personas": persona, "mensaje": "Persona Eliminada Correctamente"})

