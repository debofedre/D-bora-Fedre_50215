from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class GlosariosForm(forms.Form):
    Término_SP = forms.CharField(max_length=50, required=True)
    Término_EN = forms.CharField(max_length=50, required=True)
    
class AcrónimosForm(forms.Form):
    acrónimo = forms.CharField(max_length=100, required=True)
    definición = forms.CharField(max_length=100, required=True)
    
class GuíasForm(forms.Form):
    categoría = forms.CharField(max_length=100, required=True)
    regla = forms.CharField(max_length=100, required=True)

class HerramientasForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    caract = forms.CharField(max_length=100, required=True)
    enlace = forms.CharField(max_length=100, required=True)

class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)