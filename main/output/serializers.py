from rest_framework import serializers

from .models import Output


# Definimos un serializador para el modelo Output
class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        # Especificamos el modelo que estamos serializando
        model = Output

        # Especificamos todos los campos que queremos incluir en la representación serializada
        fields = "__all__"

        # Especificamos los campos que deben estar en modo solo lectura
        read_only_fields = ['auditor']
