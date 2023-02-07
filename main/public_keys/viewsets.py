from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PublicKeySerializer
from .models import PublicKey

# Definición de la clase PublicKeyViewSet que controla las operaciones CRUD
class PublicKeyViewSet(viewsets.ModelViewSet):
    # Conjunto de objetos PublicKey que serán usados en la vista
    queryset = PublicKey.objects.all()
    # Serializador que se usará para representar los objetos PublicKey en la API RESTful
    serializer_class = PublicKeySerializer
    # Clases de permisos que controlarán el acceso a esta vista
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
