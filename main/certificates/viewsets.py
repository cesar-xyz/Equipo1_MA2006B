from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CertificateSerializer

from .models import Certificate


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all().order_by("-created_at")
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]
