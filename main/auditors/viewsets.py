# Importar el módulo "viewsets" y "permissions" de Django Rest Framework
from rest_framework import permissions
from rest_framework import viewsets

# Importar el modelo "Auditor" desde el módulo "models"
from .models import Auditor
# Importar el serializador "AuditorSerializer" desde el módulo "serializers"
from .serializers import AuditorSerializer


# Definir la clase "AuditorViewset" que hereda de "viewsets.ModelViewSet"
class AuditorViewset(viewsets.ModelViewSet):
    # Especificar el conjunto de datos que se utilizará en el ViewSet
    queryset = Auditor.objects.all()

    # Especificar el serializador que se utilizará para convertir los datos de "Auditor"
    serializer_class = AuditorSerializer

    # Especificar los permisos necesarios para acceder a los datos en el ViewSet
    permission_classes = [permissions.IsAuthenticated]
