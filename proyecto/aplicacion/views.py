from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import UpdateView

#_____________________Home

def home(request):
    return render(request, "aplicacion/index.html")

#_____________________Acerca
def acerca(request):
    contexto = {'acerca': Acerca.objects.all()}
    return render(request, "aplicacion/acerca.html", contexto)

#_____________________Glosario + Formulario + Update + Delete

def glosarios(request):
    contexto = {'glosarios': Glosarios.objects.all().order_by("id")}#ordenado por id
    return render(request, "aplicacion/glosarios.html", contexto)

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
            contexto = {'glosarios': Glosarios.objects.all().order_by("id")}
            return render(request, "aplicacion/glosarios.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GlosariosForm()
        return render(request, "aplicacion/glosariosForm.html", {"form": miForm})

# #Update con https://ccbv.co.uk/
# class GlosariosUpdate(UpdateView):
#     model = Glosarios
#     fields = ["Término_SP", "Término_EN"]
#     success_url = reverse_lazy("glosarios")

def glosariosUpdate(request, id_glosarios):
    glosarios = Glosarios.objects.get(id=id_glosarios)
    if request.method == "POST": #Recibí la info del usuario?
        miForm = GlosariosForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            Glosarios.Término_SP = miForm.cleaned_data.get("Término_SP")
            Glosarios.Término_EN = miForm.cleaned_data.get("Término_EN")
            glosarios.save()
            #Redirects a glosarios
            return redirect(reverse_lazy('glosarios'))
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GlosariosForm(initial = {'Término_SP':Glosarios.Término_SP,'Término_EN':Glosarios.Término_EN})
        return render(request, "aplicacion/glosariosForm.html", {"form": miForm})
    
def glosariosDelete(request, id_glosarios):
    glosarios = Glosarios.objects.get(id=id_glosarios)
    glosarios.delete()
    return redirect(reverse_lazy('glosarios'))

#_____________________Buscador
    
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

#_____________________Acrónimos + Formulario + Update

def acrónimos(request):
    contexto = {'acrónimos': Acrónimos.objects.all()}
    return render(request, "aplicacion/acrónimos.html", contexto)

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
    
def acrónimosUpdate(request, id_acrónimos):
    acrónimos = Acrónimos.objects.get(id=id_acrónimos)
    if request.method == "POST": #Recibí la info del usuario?
        miForm = AcrónimosForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            Acrónimos.acrónimo = miForm.cleaned_data.get("acrónimo")
            Acrónimos.definición = miForm.cleaned_data.get("definición")
            acrónimos.save()
            #Redirects a acrónimos
            contexto = {'acrónimos': Acrónimos.objects.all().order_by("id")}
            return render(request, "aplicacion/acrónimos.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = AcrónimosForm(initial = {'acrónimo':Acrónimos.acrónimo,'definición':Acrónimos.definición})
        return render(request, "aplicacion/acrónimosForm.html", {"form": miForm})
    

def acrónimosDelete(request, id_acrónimos):
    acrónimos = Acrónimos.objects.get(id=id_acrónimos)
    acrónimos.delete()
    return redirect(reverse_lazy('acrónimos'))
    
    
#_____________________Guías + Formulario + Update

def guías(request):
    contexto = {'guías': Guías.objects.all()}
    return render(request, "aplicacion/guías.html", contexto)

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
    
def guíasUpdate(request, id_guías):
    guías = Guías.objects.get(id=id_guías)
    if request.method == "POST": #Recibí la info del usuario?
        miForm = GuíasForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            Guías.categoría = miForm.cleaned_data.get("categoría")
            Guías.regla = miForm.cleaned_data.get("regla")
            guías.save()
            #Redirects a guías
            contexto = {'guías': Guías.objects.all().order_by("id")}
            return render(request, "aplicacion/guías.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GuíasForm(initial = {'categoría':Guías.categoría,'regla':Guías.regla})
        return render(request, "aplicacion/guíasForm.html", {"form": miForm})
    
def guíasDelete(request, id_guías):
    guías = Guías.objects.get(id=id_guías)
    guías.delete()
    return redirect(reverse_lazy('guías'))
    
    
#_____________________Herramientas + Formulario + Update
    
def herramientas(request):
    contexto = {'herramientas': Herramientas.objects.all()}
    return render(request, "aplicacion/herramientas.html", contexto)

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

def herramientasUpdate(request, id_herramientas):
    herramientas = Herramientas.objects.get(id=id_herramientas)
    if request.method == "POST": #Recibí la info del usuario?
        miForm = HerramientasForm(request.POST)
        if miForm.is_valid(): #is_valid es un metodo, siempre debe ir con ()
            Herramientas.nombre = miForm.cleaned_data.get("nombre")
            Herramientas.caract = miForm.cleaned_data.get("caract")
            Herramientas.enlace = miForm.cleaned_data.get("enlace")
            herramientas.save()
            #Redirects a herramientas
            contexto = {'herramientas': Herramientas.objects.all().order_by("id")}
            return render(request, "aplicacion/herramientas.html", contexto)
         # Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = HerramientasForm(initial = {'nombre':Herramientas.nombre,'caract':Herramientas.caract, 'enlace':Herramientas.enlace})
        return render(request, "aplicacion/herramientasForm.html", {"form": miForm})

def herramientasDelete(request, id_herramientas):
    herramientas = Herramientas.objects.get(id=id_herramientas)
    herramientas.delete()
    return redirect(reverse_lazy('herramientas'))
