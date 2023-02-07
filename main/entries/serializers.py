from rest_framework import serializers
from .models import Entry

# Definir el serializador para el modelo de entrada
class EntrySerializer(serializers.ModelSerializer):
    # Especificar el modelo a ser serializado
    class Meta:
        model = Entry
        # Incluir todos los campos del modelo en la serialización
        fields = "__all__"
