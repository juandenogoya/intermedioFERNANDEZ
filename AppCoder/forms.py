from django import forms

class CursoForm (forms.Form):
    nombre = forms.CharField (label = "Nombre", max_length= 50)
    comision = forms.IntegerField (label = "Comision")

class ProfeForm (forms.Form):
    nombre = forms.CharField (label = "Nombre Profesor", max_length= 50)
    apellido = forms.CharField (label = "Apellido Profesor", max_length= 50)
    email = forms.EmailField (label = "Email Profesor")
    profesion = forms.CharField (label = "Profesion", max_length= 50)


class FutbolForm (forms.Form):
    nombre = forms.CharField(label = "Nombre Juegador", max_length= 50)
    apellido = forms.CharField(label = "Apellido Jugador", max_length=50)
    anio_nacimiento = forms.IntegerField(label= "Categoria")


class FamiliaForm (forms.Form):
    nombre = forms.CharField (label = "Nombre", max_length=60)
    apellido= forms.CharField (label = "Apellido", max_length=60)
    fecha_nacimiento = forms.DateField(label = "Fecha Nacimiento" )


class PersonaForms (forms.Form):
    nombre = forms.CharField (label = "Nombre", max_length=50)
    apellido = forms.CharField (label = "Apellido", max_length=50)
    email = forms.EmailField(label= "email")
    fechaNacimiento = forms.DateField(label= "Fecha Nacimiento")
    tieneObraSocial = forms.BooleanField(label = "Obras Social")


