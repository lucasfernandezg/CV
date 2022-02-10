from django.db import models

# Create your models here.


class Estudios(models.Model):
    institucion = models.CharField(max_length=32)
    grado = models.CharField(max_length=32)
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)
    descripcion = models.TextField(max_length=254)
    i = models.IntegerField()


class Programacion(models.Model):

    lenguaje = models.CharField(max_length=32)
    observacion = models.CharField(max_length=254)


class Trabajos(models.Model):
    institucion = models.CharField(max_length=32)
    puesto = models.CharField(max_length=32)
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)
    descripcion = models.TextField(max_length=254)
    i = models.IntegerField()
