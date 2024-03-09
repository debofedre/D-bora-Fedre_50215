from django.urls import path, include
from aplicacion.views import *

urlpatterns = [
    path('', home, name="home"),
    path('acrónimos/', acrónimos, name="acrónimos"),
    path('glosarios/', glosarios, name="glosarios"),
    path('guías/', guías, name="guías"),
    path('herramientas/', herramientas, name="herramientas"),
    path('acerca/', acerca, name="acerca"),
    #ruta para formularios
    path('glosariosForm/', glosariosForm, name="glosariosForm"),
    path('acrónimosForm/', acrónimosForm, name="acrónimosForm"),
    path('guíasForm/', guíasForm, name="guíasForm"),
    path('herramientasForm/', herramientasForm, name="herramientasForm"),
    #Buscador
    path('buscarGlosarios/', buscarGlosarios, name="buscarGlosarios"),
    path('encontrarGlosarios/', encontrarGlosarios, name="encontrarGlosarios"),
]
