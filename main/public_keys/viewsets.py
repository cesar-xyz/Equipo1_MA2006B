from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PublicKeySerializer

from .models import PublicKey


class PublicKeyViewSet(viewsets.ModelViewSet):
    queryset = PublicKey.objects.all()
    serializer_class = PublicKeySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
