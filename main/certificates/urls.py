from rest_framework import routers

from .viewsets import CertificateViewSet

router = routers.DefaultRouter()
router.register("certificates", CertificateViewSet)
