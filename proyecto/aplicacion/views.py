from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/index.html")

def glosario(request):
    contexto = {'glosario': Glosario.objects.all()}
    return render(request, "aplicacion/glosario.html", contexto)

def guías(request):
    return render(request, "aplicacion/guías.html")

def consultas(request):
    return render(request, "aplicacion/consultas.html")

def herramientas(request):
    return render(request, "aplicacion/herramientas.html")