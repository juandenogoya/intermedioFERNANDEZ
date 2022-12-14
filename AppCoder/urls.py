from django.urls import path
from .views import *



urlpatterns = [
    path('curso/', cursos, name ='curso'),
    path('estudiantes/', estudiantes, name ='estudiantes'),
    path('profesores/', profesores, name ='profesores'),
    path('entregables/', entregables, name ='entregables'),
    path('', inicio, name ='inicio')



]