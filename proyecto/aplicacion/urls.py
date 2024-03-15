from django.urls import path, include
from aplicacion.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #adicionales
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),
    
    #_________glosarios
    path('glosarios/', glosarios, name="glosarios"),
    
    #form, update y delete de glosarios
    path('glosariosForm/', glosariosForm, name="glosariosForm"),
    #path('glosariosUpdate/<id_glosarios>/', glosariosUpdate, name="glosariosUpdate"),
    path('glosariosUpdate/<int:pk>/', GlosariosUpdate.as_view(), name="glosariosUpdate"),
    path('glosariosDelete/<id_glosarios>/', glosariosDelete, name="glosariosDelete"),
    
    #buscador de glosarios
    path('buscarGlosarios/', buscarGlosarios, name="buscarGlosarios"),
    path('encontrarGlosarios/', encontrarGlosarios, name="encontrarGlosarios"),
    
    #_________acrónimos
    path('acrónimos/', acrónimos, name="acrónimos"),
    
     #form, update y delete de acrónimos
    path('acrónimosForm/', acrónimosForm, name="acrónimosForm"),
    #path('acrónimosUpdate/<id_acrónimos>/', acrónimosUpdate, name="acrónimosUpdate"),
    path('acrónimosUpdate/<int:pk>/', AcrónimosUpdate.as_view(), name="acrónimosUpdate"),
    path('acrónimosDelete/<id_acrónimos>/', acrónimosDelete, name="acrónimosDelete"),
    
    #_________herramientas
    path('herramientas/', herramientas, name="herramientas"),
    
     #form, update y delete de herramientas
    path('herramientasForm/', herramientasForm, name="herramientasForm"),
    #path('herramientasUpdate/<id_herramientas>/', herramientasUpdate, name="herramientasUpdate"),
    path('herramientasUpdate/<int:pk>/', HerramientasUpdate.as_view(), name="herramientasUpdate"),
    path('herramientasDelete/<id_herramientas>/', herramientasDelete, name="herramientasDelete"),
    
    #_________guías
    path('guías/', guías, name="guías"),
    
     #form, update y delete de guías
    path('guíasForm/', guíasForm, name="guíasForm"),
    #path('guíasUpdate/<id_guías>/', guíasUpdate, name="guíasUpdate"),
    path('guíasUpdate/<int:pk>/', GuíasUpdate.as_view(), name="guíasUpdate"),
    path('guíasDelete/<id_guías>/', guíasDelete, name="guíasDelete"),
    
     #____________________ Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),

    path('registrar/', register, name="registrar"),
]
