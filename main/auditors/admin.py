"""
 La función admin.register se utiliza para registrar la clase "AuditorAdmin"
 con la administración de Django. Esto significa que el modelo "Auditor"
 se mostrará en la interfaz de administración de Django y se puede administrar
 a través de la clase "AuditorAdmin".
 """

# Importar la clase de administración de Django
from django.contrib import admin

# Importar el modelo "Auditor" desde el módulo de models.py
from .models import Auditor


# Decorar la clase "AuditorAdmin" con @admin.register para registrarla con la administración de Django
@admin.register(Auditor)
# Definir la clase "AuditorAdmin" que hereda de "admin.ModelAdmin"
class AuditorAdmin(admin.ModelAdmin):
    # Definir una lista de campos que se mostrarán en la lista de registros en la interfaz de administración
    list_display = ["name", "mac_address"]

    # Definir una lista de campos en los que se puede buscar en la interfaz de administración
    search_fields = ["name", "mac_address"]
