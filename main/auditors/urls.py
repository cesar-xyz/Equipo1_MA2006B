# Importar el módulo de routers de Django Rest Framework
from rest_framework import routers

# Importar el ViewSet "AuditorViewset" desde el módulo de viewsets
from .viewsets import AuditorViewset

# Crear una instancia del router por defecto
router = routers.DefaultRouter()

# Registrar el ViewSet "AuditorViewset" con la API
router.register("auditors", AuditorViewset)
