from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AuditorSerializer

from .models import Auditor


class AuditorViewset(viewsets.ModelViewSet):
    queryset = Auditor.objects.all().order_by("-created_at")
    serializer_class = AuditorSerializer
    permission_classes = [permissions.IsAuthenticated]
