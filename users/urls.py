from rest_framework import routers

from users.viewsets import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
