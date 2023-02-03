from rest_framework import routers

from .viewsets import PublicKeyViewSet

router = routers.DefaultRouter()
router.register("public_keys", PublicKeyViewSet)
