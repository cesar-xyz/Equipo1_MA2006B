from django.contrib import admin

from .models import Output


# Registramos la clase OutputAdmin como un administrador para el modelo Output
@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    # Especificamos los campos que se mostrarán en la lista de objetos de salida
    list_display = ['out_auditor', 'message', 'received']
    # Especificamos los campos que se usarán para la búsqueda
    search_fields = ['out_auditor', 'message', 'received']
