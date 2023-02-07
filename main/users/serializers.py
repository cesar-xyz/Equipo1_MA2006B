from rest_framework import serializers
from users.models import User

# Creamos una clase de serializador que hereda de ModelSerializer
class UserSerializer(serializers.ModelSerializer):
    # Definimos la información de Meta para el serializador
    class Meta:
        # Establecemos el modelo que se va a serializar
        model = User
        # Establecemos los campos que se incluirán en la representación serializada
        fields = "__all__"
