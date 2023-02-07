from rest_framework import routers
from .viewsets import OutputViewset

# Creamos una instancia del router DefaultRouter
router = routers.DefaultRouter()

# Registramos la vista OutputViewset con el router
router.register("out_auditors", OutputViewset)
