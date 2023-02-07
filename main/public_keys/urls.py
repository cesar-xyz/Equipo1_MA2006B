from rest_framework import routers
from .viewsets import PublicKeyViewSet

# Crear una instancia de DefaultRouter
router = routers.DefaultRouter()

# Registrar la vista PublicKeyViewSet en el enrutador
router.register("public_keys", PublicKeyViewSet)
