from django.db import models
from django.contrib import admin

class Cursos(models.Model):
    nombrecursos = models.CharField(max_length=100)

    def __str__(self):
        return self.nombrecursos

class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Boleta(models.Model):
    calificaciones = models.CharField(max_length=5)
    Curso = models.ManyToManyField(Cursos)
    Alumno = models.ForeignKey(Alumnos)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.calificaciones
