from rest_framework import routers

from .viewsets import OutputViewset

router = routers.DefaultRouter()
router.register("out_auditors", OutputViewset)
