from rest_framework import routers

from users.viewsets import UserViewSet

# Creamos una instancia del enrutador predeterminado de Django Rest Framework
router = routers.DefaultRouter()

# Registramos el conjunto de vistas UserViewSet en el enrutador con la ruta "users"
router.register("users", UserViewSet)
