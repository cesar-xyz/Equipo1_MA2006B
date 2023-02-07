from rest_framework import serializers
from public_keys.models import PublicKey

# Serializador para la clase PublicKey
class PublicKeySerializer(serializers.ModelSerializer):
    # Definir el modelo que se usará en el serializador
    class Meta:
        model = PublicKey
        # Campos que se incluirán en la serialización
        fields = "__all__"
