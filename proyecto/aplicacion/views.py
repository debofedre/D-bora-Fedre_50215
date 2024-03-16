from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#_____________________ Home

def home(request):
    return render(request, "aplicacion/index.html")

#_____________________ Acerca
def acerca(request):
    contexto = {'acerca': Acerca.objects.all()}
    return render(request, "aplicacion/acerca.html", contexto)

#_____________________ Glosario
@login_required
def glosarios(request):
    contexto = {'glosarios': Glosarios.objects.all().order_by("id")}#ordenado por id
    return render(request, "aplicacion/glosarios.html", contexto)

# __ Form del glosario
@login_required
def glosariosForm(request):
    if request.method == "POST":
        # __ Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = GlosariosForm(request.POST)
        if miForm.is_valid(): #__ is_valid es un metodo, siempre debe ir con ()
            término_SP = miForm.cleaned_data.get("Término_SP")
            término_EN = miForm.cleaned_data.get("Término_EN")
            glosarios = Glosarios(Término_SP=término_SP, Término_EN=término_EN)
            glosarios.save()
            #__ Redirects a glosarios
            contexto = {'glosarios': Glosarios.objects.all().order_by("id")}
            return render(request, "aplicacion/glosarios.html", contexto)
         # __ Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GlosariosForm()
        return render(request, "aplicacion/glosarios_form.html", {"form": miForm})

#__ Update con https://ccbv.co.uk/ del glosario
class GlosariosUpdate(UpdateView, LoginRequiredMixin):
    model = Glosarios
    fields = ["Término_SP", "Término_EN"]
    success_url = reverse_lazy("glosarios")

#__ Delete del glosario
@login_required  
def glosariosDelete(request, id_glosarios):
    glosarios = Glosarios.objects.get(id=id_glosarios)
    glosarios.delete()
    return redirect(reverse_lazy('glosarios'))

#__ Buscador del glosario
@login_required 
def buscarGlosarios(request):
    return render(request, "aplicacion/buscarGlosarios.html")
def encontrarGlosarios(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        glosarios = Glosarios.objects.filter(Término_SP__icontains=patron)
        contexto = { "glosarios": glosarios}
        return render(request, "aplicacion/glosarios.html", contexto)
    #__ si no enceuntra nada, redirects a todo el glosario
    contexto = {'glosarios': Glosarios.objects.all()}
    return render(request, "aplicacion/glosarios.html", contexto)

#_____________________ Acrónimos
@login_required
def acrónimos(request):
    contexto = {'acrónimos': Acrónimos.objects.all()}
    return render(request, "aplicacion/acrónimos.html", contexto)

#__ Form de los acrónimos
@login_required
def acrónimosForm(request):
    if request.method == "POST":
        # __ Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = AcrónimosForm(request.POST)
        if miForm.is_valid(): # __ is_valid es un metodo, siempre debe ir con ()
            acrónimo= miForm.cleaned_data.get("acrónimo")
            definición = miForm.cleaned_data.get("definición")
            acrónimos = Acrónimos(acrónimo=acrónimo, definición=definición)
            acrónimos.save()
            # __ Redirects a acrónimos
            contexto = {'acrónimos': Acrónimos.objects.all()}
            return render(request, "aplicacion/acrónimos.html", contexto)
         # __ Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = AcrónimosForm()
        return render(request, "aplicacion/acrónimos_form.html", {"form": miForm})

#__ Update con https://ccbv.co.uk/ de los acrónimos
class AcrónimosUpdate(UpdateView, LoginRequiredMixin):
    model = Acrónimos
    fields = ["acrónimo", "definición"]
    success_url = reverse_lazy("acrónimos")
    
# __ Delete de los acrónimos    
@login_required
def acrónimosDelete(request, id_acrónimos):
    acrónimos = Acrónimos.objects.get(id=id_acrónimos)
    acrónimos.delete()
    return redirect(reverse_lazy('acrónimos'))
    
#_____________________ Guías
@login_required
def guías(request):
    contexto = {'guías': Guías.objects.all()}
    return render(request, "aplicacion/guías.html", contexto)

def guíasForm(request):
    if request.method == "POST":
        # __ Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = GuíasForm(request.POST)
        if miForm.is_valid(): # __ is_valid es un metodo, siempre debe ir con ()
            regla= miForm.cleaned_data.get("regla")
            categoría = miForm.cleaned_data.get("categoría")
            guía = Guías(regla=regla, categoría=categoría)
            guía.save()
            # __ Redirects a guías
            contexto = {'guías': Guías.objects.all()}
            return render(request, "aplicacion/guías.html", contexto)
         # __ Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = GuíasForm()
        return render(request, "aplicacion/guías_form.html", {"form": miForm})

# __ Update con https://ccbv.co.uk/ de las guías
class GuíasUpdate(UpdateView):
    model = Guías
    fields = ["categoría", "regla"]
    success_url = reverse_lazy("guías")
    
# __ Delete de las guías
def guíasDelete(request, id_guías):
    guías = Guías.objects.get(id=id_guías)
    guías.delete()
    return redirect(reverse_lazy('guías'))
    
    
#_____________________ Herramientas
@login_required
def herramientas(request):
    contexto = {'herramientas': Herramientas.objects.all()}
    return render(request, "aplicacion/herramientas.html", contexto)

def herramientasForm(request):
    if request.method == "POST":
        # __ Si ingresa en el if, es la 2nda o enésima vez que ingresa al formulario
        miForm = HerramientasForm(request.POST)
        if miForm.is_valid(): # __ is_valid es un metodo, siempre debe ir con ()
            Nombre= miForm.cleaned_data.get("Nombre")
            Descripción = miForm.cleaned_data.get("Descripción")
            Enlace = miForm.cleaned_data.get("Enlace")
            herramientas = Herramientas(Nombre=Nombre, Descripción=Descripción, Enlace=Enlace)
            herramientas.save()
            # __ Redirects a herramientas
            contexto = {'herramientas': Herramientas.objects.all()}
            return render(request, "aplicacion/herramientas.html", contexto)
         # __ Si ingresa en el else, es la 1era vez que ingresa al formulario
    else:
        miForm = HerramientasForm()
        return render(request, "aplicacion/herramientas_form.html", {"form": miForm})

# __ Update con https://ccbv.co.uk/ de las herramientas
class HerramientasUpdate(UpdateView):
    model = Herramientas
    fields = ["Nombre", "Descripción", "Enlace"]
    success_url = reverse_lazy("herramientas")

# __ Delete de las herramientas
def herramientasDelete(request, id_herramientas):
    herramientas = Herramientas.objects.get(id=id_herramientas)
    herramientas.delete()
    return redirect(reverse_lazy('herramientas'))

#_____________________ Login, logout, authentication, registration
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            
              #__ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
                
                #__________________________________________
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} ) 


@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
     template_name = "aplicacion/cambiar_clave.html"
     success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )   