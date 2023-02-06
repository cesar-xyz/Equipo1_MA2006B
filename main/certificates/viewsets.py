from rest_framework import permissions
from rest_framework import viewsets

from .models import Certificate
from .serializers import CertificateSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        certificates = super().get_queryset()
        certificates = [certificate for certificate in certificates if certificate.check_expiry()]
        return certificates
