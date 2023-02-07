from django.contrib import admin

from .models import PublicKey


# Registrar el modelo PublicKey en el panel de administración de Django
@admin.register(PublicKey)
# Clase que controla la representación y funcionalidades del modelo en el panel de administración
class PublicKeyAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos PublicKey en el panel de administración
    list_display = [
        "algorithm",
        "key",
    ]
    # Campos en los que se buscará al filtrar objetos PublicKey en el panel de administración
    search_fields = [
        "key",
        "algorithm",
    ]
