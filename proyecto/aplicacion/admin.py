from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Glosarios)
admin.site.register(Acrónimos)
admin.site.register(Acerca)
admin.site.register(Guías)
admin.site.register(Herramientas)
