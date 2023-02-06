from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ControlCenterSerializer

from .models import ControlCenter


class ControlCenterViewset(viewsets.ModelViewSet):
    queryset = ControlCenter.objects.all()
    serializer_class = ControlCenterSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
