from certificates.models import Certificate
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Entry
from .serializers import EntrySerializer

# Definir una clase EntryViewSet que gestiona los objetos Entry
class EntryViewSet(viewsets.ModelViewSet):
    # Asignar un queryset con todos los objetos Entry de la base de datos
    queryset = Entry.objects.all()
    # Asignar la clase EntrySerializer como el serializador utilizado por la clase
    serializer_class = EntrySerializer
    # Definir que los permisos necesarios para acceder a los métodos de la clase son estar autenticado
    permission_classes = [permissions.IsAuthenticated]

    # Método que se ejecuta antes de crear un nuevo objeto Entry
    def perform_create(self, serializer):
        # Obtener el nombre del auditor a partir de los datos enviados en la solicitud
        auditor = self.request.data.get('auditor')
        # Buscar el primer certificado asociado al auditor
        certificate = Certificate.objects.filter(auditor__id=auditor).first()
        # Comprobar si existe un certificado asociado al auditor
        if certificate:
            # Comprobar si el certificado ha caducado
            if certificate.check_expiry():
                # Guardar el nuevo objeto Entry
                serializer.save()
            else:
                # Lanzar una excepción ValidationError si el certificado ha caducado
                raise ValidationError("Certificate has expired.")
        else:
            # Lanzar una excepción ValidationError si no se encuentra un certificado asociado al auditor
            raise ValidationError("No matching certificate found for the given auditor_id")
