# Este serializador se utiliza para convertir datos de modelos en formato JSON
# para su transferencia a través de la API.

# Importar el módulo de serializadores de Django Rest Framework
from rest_framework import serializers

# Importar el modelo "Auditor" desde el módulo de models.py
from .models import Auditor


# Definir la clase "AuditorSerializer" que hereda de "serializers.ModelSerializer"
class AuditorSerializer(serializers.ModelSerializer):
    # Definir la clase Meta que contiene información adicional sobre la configuración del serializador
    class Meta:
        # Especificar el modelo del cual se creará el serializador
        model = Auditor
        # Especificar una lista de campos que se incluirán en la salida del serializador
        fields = "__all__"
