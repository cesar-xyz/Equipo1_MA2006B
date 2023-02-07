from django.contrib import admin

from .models import Entry

# Decorador que registra la clase EntryAdmin para administrar objetos Entry
@admin.register(Entry)
# Definir una clase EntryAdmin que gestiona los objetos Entry
class EntryAdmin(admin.ModelAdmin):
    # Lista de campos que se mostrarán en la lista de objetos Entry en la interfaz de administración
    list_display = ('id', 'date', 'auditor', 'is_producing', 'quantity')
    # Lista de campos que se utilizarán para la búsqueda de objetos Entry en la interfaz de administración
    search_fields = ('id', 'date')