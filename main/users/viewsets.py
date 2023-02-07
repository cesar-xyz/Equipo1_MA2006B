from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    Conjunto de vistas de API para el modelo de usuario.
    Permite ver y editar objetos de usuario a través de la API.
    """

    # Definimos el queryset que se utilizará para obtener objetos de usuario
    queryset = User.objects.all().order_by("-date_joined")

    # Definimos el serializador que se utilizará para representar objetos de usuario
    serializer_class = UserSerializer

    # Definimos los permisos requeridos para acceder a este conjunto de vistas
    permission_classes = [permissions.IsAuthenticated]
