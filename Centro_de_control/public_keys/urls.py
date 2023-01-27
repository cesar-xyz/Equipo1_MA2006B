from rest_framework import routers

from public_keys.viewsets import PublicKeyViewSet

router = routers.DefaultRouter()
router.register("public_keys", PublicKeyViewSet)
