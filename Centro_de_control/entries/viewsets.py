from rest_framework import viewsets
from rest_framework import permissions
from entries.serializers import EntrySerializer

from entries.models import Entry


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by("-created_at")
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
