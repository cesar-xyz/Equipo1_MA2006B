from rest_framework import permissions
from rest_framework import viewsets

from .models import Output
from .serializers import OutputSerializer
from rest_framework.exceptions import ValidationError
from certificates.models import Certificate

class OutputViewset(viewsets.ModelViewSet):
    queryset = Output.objects.all()
    serializer_class = OutputSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        auditor = self.request.data.get('out_auditor')
        message = self.request.data.get('message')
        certificate = Certificate.objects.filter(auditor__id=auditor).first()
        if certificate:
            if certificate.check_expiry():
                return message
            else:
                raise ValidationError("Certificate has expired.")
        else:
            raise ValidationError("No matching certificate found for the given auditor_id")
