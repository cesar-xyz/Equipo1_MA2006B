from rest_framework import routers

from .viewsets import ControlCenterViewset

router = routers.DefaultRouter()
router.register("control_center", ControlCenterViewset)
