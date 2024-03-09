from django.db import models

# Create your models here.

class Glosario(models.Model):
    termEN = models.CharField(max_length=100)
    termSP = models.CharField(max_length=100)

class Guías(models.Model):
    regla = models.CharField(max_length=100)
    categoría = models.CharField(max_length=100)

class Consultas(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    consulta = models.CharField(max_length=100)

class Herramientas(models.Model):
    nombre = models.CharField(max_length=100)
    caract = models.CharField(max_length=100)
