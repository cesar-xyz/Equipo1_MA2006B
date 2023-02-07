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

    # Sobreescribimos el método get_queryset para proporcionar comportamiento personalizado
    def get_queryset(self):
        # Obtenemos el valor del campo out_auditor de la solicitud
        auditor = self.request.data.get('out_auditor')
        # Obtenemos el valor del campo message de la solicitud
        message = self.request.data.get('message')
        # Buscamos un objeto Certificate que coincida con el auditor_id
        certificate = Certificate.objects.filter(auditor__id=auditor).first()
        # Si se encuentra un certificado
        if certificate:
            # Verificamos si ha expirado
            if certificate.check_expiry():
                return message
            else:
                # Si ha expirado, levantamos una excepción de validación
                raise ValidationError("Certificate has expired.")
        else:
            # Si no se encuentra un certificado, levantamos una excepción de validación
            raise ValidationError("No matching certificate found for the given auditor_id")
