from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
 
    def __str__(self):
        return self.nombre
 
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    legajo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
