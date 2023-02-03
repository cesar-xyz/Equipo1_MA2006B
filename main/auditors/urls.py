from rest_framework import routers

from .viewsets import AuditorViewset

router = routers.DefaultRouter()
router.register("auditors", AuditorViewset)
