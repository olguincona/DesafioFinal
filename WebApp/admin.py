from django.contrib import admin
from .models import Productos,Comprador,Vendedor,Devolucion,Profile

admin.site.register(Productos)
admin.site.register(Comprador)
admin.site.register(Vendedor)
admin.site.register(Devolucion)
admin.site.register(Profile)


