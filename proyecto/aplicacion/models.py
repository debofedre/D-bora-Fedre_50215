from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Glosarios(models.Model):
    Término_EN = models.CharField(max_length=100)
    Término_SP = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Glosarios"
        verbose_name_plural = "Glosarios"
    
    def __str__(self):
        return f"{self.Término_EN}, {self.Término_SP}"

class Guías(models.Model):
    regla = models.CharField(max_length=100)
    categoría = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["categoría"]
        verbose_name = "Guías"
        verbose_name_plural = "Guías"
    
    def __str__(self):
        return f"{self.regla}, {self.categoría}"

class Acrónimos(models.Model):
    acrónimo = models.CharField(max_length=100)
    definición = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["acrónimo"]
        verbose_name = "Acrónimos"
        verbose_name_plural = "Acrónimos"
    
    def __str__(self):
        return f"{self.acrónimo}, {self.definición}"

class Herramientas(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripción = models.CharField(max_length=500)
    Enlace = models.CharField(max_length=100, default="Valor por defecto")
    
    class Meta:
        verbose_name = "Herramientas"
        verbose_name_plural = "Herramientas"
    
    def __str__(self):
        return f"{self.nombre}, {self.Descripción}, {self.Enlace}"
    
class Acerca(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Acerca"
        verbose_name_plural = "Acerca"
    
    def __str__(self):
        return f"{self.nombre}, {self.email}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.imagen}"