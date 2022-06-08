from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellidade = models.CharField(max_length=30)
    emails = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidade = models.CharField(max_length=30)
    emails = models.EmailField()
    profesion = models.CharField(max_length=30)


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntregable = models.DateField()
    entregado = models.BooleanField()