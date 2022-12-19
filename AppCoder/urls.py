from django.urls import path
from .views import *



urlpatterns = [
    path('curso/', cursos, name ='curso'),
    path('estudiantes/', estudiantes, name ='estudiantes'),
    path('profesores/', profesores, name ='profesores'),
    path('entregables/', entregables, name ='entregables'),
    path('', inicio, name ='inicio'),
    path('familia/', familiar, name = 'familia'),
    path('familiaFormulario', familiaFormulario, name = 'familiaFormulario'),
    path('cursoFormulario/', cursoFormulario, name = 'cursoFormulario'),
    path('profeFormulario/', profeFormulario, name = 'profeFormulario'),
    path('futbol/', futbol, name = 'futbol'),
    path('futbolFormulario/', futbolFormulario, name = 'futbolFormulario'),



]