from django import forms 

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