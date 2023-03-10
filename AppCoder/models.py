from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__ (self):
        return f'{self.nombre} - {str(self.comision)}'

class Estudiante (models.Model):
    nombre = models.CharField (max_length=60)
    apellido= models.CharField (max_length=60)
    email = models.EmailField()

    def __str__ (self):
        return f'{self.nombre} - {self.apellido}'

class Profesor (models.Model):
    nombre = models.CharField (max_length=60)
    apellido= models.CharField (max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.nombre} - {self.apellido}'

class Entregable (models.Model):
    nombre = models.CharField (max_length=60)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__ (self):
        return f'{self.nombre} - {self.entregado}'

class Familiar (models.Model):
    nombre = models.CharField (max_length=60)
    apellido= models.CharField (max_length=60)
    fecha_nacimiento = models.DateField()

    def __str__ (self):
        return f' {self.nombre} - {self.apellido} - Nacimiento: {self.fecha_nacimiento}'

#MODELO de FUTBOL
class Futbol (models.Model):
    nombre = models.CharField (max_length=60)
    apellido= models.CharField (max_length=60)
    anio_nacimiento = models.IntegerField()


    def __str__ (self):
        return f' {self.nombre} - {self.apellido} - Categoria: {self.anio_nacimiento}'


#MODELO de PERSONA
class Persona (models.Model):
    nombre = models.CharField (max_length= 50)
    apellido = models.CharField (max_length= 50)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    tieneObraSocial = models.BooleanField()

    def __str__ (self):
        return f"{self.nombre} - {self.apellido}"




