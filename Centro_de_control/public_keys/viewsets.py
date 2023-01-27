from rest_framework import viewsets
from rest_framework import permissions
from public_keys.serializers import PublicKeySerializer

from public_keys.models import PublicKey


class PublicKeyViewSet(viewsets.ModelViewSet):
    queryset = PublicKey.objects.all().order_by("-created_at")
    serializer_class = PublicKeySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
