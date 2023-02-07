# Importar las clases necesarias de los módulos de Django
from django.db import models
from django.utils.translation import gettext as _


# Crear una clase "Auditor" que hereda de la clase "Paranoid"
class Auditor(models.Model):
    # Definir el campo "name" como un campo de tipo CharField
    # con un tamaño máximo de 128 caracteres y una etiqueta de "name"
    name = models.CharField(_("name"), max_length=128, unique=True)

    # Definir el campo "mac_address" como un campo de tipo CharField
    # con un tamaño máximo de 256 caracteres y una etiqueta de "mac address"
    mac_address = models.CharField(_("mac address"), max_length=256)

    # Definir la clase Meta para proporcionar información adicional sobre el modelo
    class Meta:
        # Establecer el nombre verbal para una sola instancia del modelo como "auditor"
        verbose_name = _("auditor")
        # Establecer el nombre verbal para varias instancias del modelo como "auditors"
        verbose_name_plural = _("auditors")

    # Definir el método __str__ para devolver una representación en cadena de una instancia del modelo
    def __str__(self):
        # Devolver "Auditor: [nombre del auditor]"
        return f"Auditor: {self.name}"
