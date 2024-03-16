from django.urls import path, include
from aplicacion.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #_____________________ Adicionales
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),
    
    #_____________________ Glosarios
    path('glosarios/', glosarios, name="glosarios"),
    # __ form
    path('glosariosForm/', glosariosForm, name="glosariosForm"),
    # __ update
    path('glosariosUpdate/<int:pk>/', GlosariosUpdate.as_view(), name="glosariosUpdate"),
    # __ delete
    path('glosariosDelete/<id_glosarios>/', glosariosDelete, name="glosariosDelete"),
    # __ buscador
    path('buscarGlosarios/', buscarGlosarios, name="buscarGlosarios"),
    path('encontrarGlosarios/', encontrarGlosarios, name="encontrarGlosarios"),
    
    #_____________________ Acrónimos
    path('acrónimos/', acrónimos, name="acrónimos"),
    # __ form
    path('acrónimosForm/', acrónimosForm, name="acrónimosForm"),
    # __ update
    path('acrónimosUpdate/<int:pk>/', AcrónimosUpdate.as_view(), name="acrónimosUpdate"),
    # __ delete
    path('acrónimosDelete/<id_acrónimos>/', acrónimosDelete, name="acrónimosDelete"),
    
    #_____________________ Herramientas
    path('herramientas/', herramientas, name="herramientas"),
    # __ form
    path('herramientasForm/', herramientasForm, name="herramientasForm"),
    # __ update
    path('herramientasUpdate/<int:pk>/', HerramientasUpdate.as_view(), name="herramientasUpdate"),
    # __ delete
    path('herramientasDelete/<id_herramientas>/', herramientasDelete, name="herramientasDelete"),
    
    #_____________________ Guías
    path('guías/', guías, name="guías"),
    # __ form
    path('guíasForm/', guíasForm, name="guíasForm"),
    # __ update
    path('guíasUpdate/<int:pk>/', GuíasUpdate.as_view(), name="guíasUpdate"),
    # __ delete
    path('guíasDelete/<id_guías>/', guíasDelete, name="guíasDelete"),
    
    #_____________________ Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),
    
    #_____________________ Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]
