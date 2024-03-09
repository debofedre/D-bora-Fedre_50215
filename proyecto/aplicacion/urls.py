from django.urls import path, include
from aplicacion.views import *

urlpatterns = [
    path('', home, name="home"),
    path('consultas/', consultas, name="consultas"),
    path('glosario/', glosario, name="glosario"),
    path('guías/', guías, name="guías"),
    path('herramientas/', herramientas, name="herramientas"),
]
