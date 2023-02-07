from certificates.models import Certificate
from rest_framework import permissions
from rest_framework import viewsets

from .models import Output
from .serializers import OutputSerializer


# Definimos una vista OutputViewset que es una subclase de viewsets.ModelViewSet

class OutputViewset(viewsets.ModelViewSet):
    # Especificamos el conjunto de objetos que la vista manipulará
    queryset = Output.objects.all()
    # Especificamos el serializador que se usará
    serializer_class = OutputSerializer
    # Especificamos las clases de permisos que se aplicarán a la vista
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # certificates = super().get_queryset()
        # certificates = [certificate for certificate in certificates if certificate.check_expiry()]
        auditor = self.request.GET.get('auditor')
        # TODO: No regresa el id del auditor, solo funciona con el Audiror 1 por mientras
        # auditor = Auditor.objects.get(id=auditor_id)
        certificate = Certificate.objects.get(auditor__name='Auditor 1')
        check = certificate.check_expiry()
        if check:
            outputs = super().get_queryset()
        else:
            outputs = []
        return outputs
