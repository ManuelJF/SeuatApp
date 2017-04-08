from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Matricula(models.Model):
    clave = models.CharField(max_length=100)

    def __str__(self):
        return self.clave

class Materia(models.Model):
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.clave

class Grupo(models.Model):
    grupo = models.CharField(max_length=100)

    def __str__(self):
        return self.grupo

class Grado(models.Model):
    grado = models.CharField(max_length=100)

    def __str__(self):
        return self.grado

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    matricula = models.ForeignKey(Matricula)
    grado = models.ForeignKey(Grado)
    grupo = models.ForeignKey(Grupo)

    def __str__(self):
        return self.user.first_name

class Carrera(models.Model):
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=250)
    tipo = models.BooleanField(default=False)
    materia = models.ForeignKey(Materia)
    alumno = models.ForeignKey(Alumno)

    def __str__(self):
        return self.clave
