from django.shortcuts import render

from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "aplicacion/index.html")

def glosarios(request):
    contexto = {'glosarios': Glosarios.objects.all()}
    return render(request, "aplicacion/glosarios.html", contexto)

def guías(request):
    contexto = {'guías': Guías.objects.all()}
    return render(request, "aplicacion/guías.html", contexto)

def acrónimos(request):
    contexto = {'acrónimos': Acrónimos.objects.all()}
    return render(request, "aplicacion/acrónimos.html", contexto)

def herramientas(request):
    contexto = {'herramientas': Herramientas.objects.all()}
    return render(request, "aplicacion/herramientas.html", contexto)

#Adicional
def acerca(request):
    contexto = {'acerca': Acerca.objects.all()}
    return render(request, "aplicacion/acerca.html", contexto)

#Formulario glosario

def glosariosForm(request):
    if request.method == "POST":
        # Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = GlosariosForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            término_SP = miForm.cleaned_data.get("Término_SP")
            término_EN = miForm.cleaned_data.get("Término_EN")
            glosarios = Glosarios(Término_SP=término_SP, Término_EN=término_EN)
            glosarios.save()
            #Redirects a glosarios
            contexto = {'glosarios': Glosarios.objects.all()}
            return render(request, "aplicacion/glosarios.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GlosariosForm()
        return render(request, "aplicacion/glosariosForm.html", {"form": miForm})

#Formulario acrónimos

def acrónimosForm(request):
    if request.method == "POST":
        # Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = AcrónimosForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            acrónimo= miForm.cleaned_data.get("acrónimo")
            definición = miForm.cleaned_data.get("definición")
            acrónimos = Acrónimos(acrónimo=acrónimo, definición=definición)
            acrónimos.save()
            #Redirects a acrónimos
            contexto = {'acrónimos': Acrónimos.objects.all()}
            return render(request, "aplicacion/acrónimos.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = AcrónimosForm()
        return render(request, "aplicacion/acrónimosForm.html", {"form": miForm})
    
    
#Formulario guías

def guíasForm(request):
    if request.method == "POST":
        # Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = GuíasForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            regla= miForm.cleaned_data.get("regla")
            categoría = miForm.cleaned_data.get("categoría")
            guía = Guías(regla=regla, categoría=categoría)
            guía.save()
            #Redirects a guías
            contexto = {'guías': Guías.objects.all()}
            return render(request, "aplicacion/guías.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GuíasForm()
        return render(request, "aplicacion/guíasForm.html", {"form": miForm})
    
    
    #Formulario herramientas

def herramientasForm(request):
    if request.method == "POST":
        # Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = HerramientasForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            nombre= miForm.cleaned_data.get("nombre")
            caract = miForm.cleaned_data.get("caract")
            enlace = miForm.cleaned_data.get("enlace")
            herramientas = Herramientas(nombre=nombre, caract=caract, enlace=enlace)
            herramientas.save()
            #Redirects a herramientas
            contexto = {'herramientas': Herramientas.objects.all()}
            return render(request, "aplicacion/herramientas.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = HerramientasForm()
        return render(request, "aplicacion/herramientasForm.html", {"form": miForm})
    
    #Búsqueda
    
def buscarGlosarios(request):
    return render(request, "aplicacion/buscarGlosarios.html")
def encontrarGlosarios(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        glosarios = Glosarios.objects.filter(Término_SP__icontains=patron)
        contexto = { "glosarios": glosarios}
        return render(request, "aplicacion/glosarios.html", contexto)
    #si no enceuntra nada, redirects a todo el glosario
    contexto = {'glosarios': Glosarios.objects.all()}
    return render(request, "aplicacion/glosarios.html", contexto)
