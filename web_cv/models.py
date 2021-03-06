from django.db import models

# Create your models here.


class Estudios(models.Model):
    institucion = models.CharField(max_length=32)
    grado = models.CharField(max_length=32)
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)
    descripcion = models.TextField(max_length=254)
    descripcion_en = models.TextField(max_length=254, default="Test")
    i = models.IntegerField()

    def __str__(self):
        return self.institucion


class Programacion(models.Model):

    lenguaje = models.CharField(max_length=32)
    observacion = models.CharField(max_length=254)


class Trabajos(models.Model):
    institucion = models.CharField(max_length=32)
    puesto = models.CharField(max_length=32)
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)
    descripcion = models.TextField(max_length=254)
    descripcion_en = models.TextField(max_length=254, default="Test")
    i = models.IntegerField()

    def __str__(self):
        return self.institucion
