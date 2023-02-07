from rest_framework import permissions
from rest_framework import viewsets

from .models import Output
from .serializers import OutputSerializer
from rest_framework.exceptions import ValidationError
from certificates.models import Certificate

# Definimos una vista OutputViewset que es una subclase de viewsets.ModelViewSet
class OutputViewset(viewsets.ModelViewSet):
    # Especificamos el conjunto de objetos que la vista manipulará
    queryset = Output.objects.all()
    # Especificamos el serializador que se usará
    serializer_class = OutputSerializer
    # Especificamos las clases de permisos que se aplicarán a la vista
    permission_classes = [permissions.IsAuthenticated]
