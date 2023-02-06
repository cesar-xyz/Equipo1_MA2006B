from certificates.models import Certificate
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        auditor = self.request.data.get('auditor')
        certificate = Certificate.objects.filter(auditor__name=auditor).first()
        if certificate:
            if certificate.check_expiry():
                serializer.save()
            else:
                raise ValidationError("Certificate has expired.")
        else:
            raise ValidationError("No matching certificate found for the given auditor_id")
