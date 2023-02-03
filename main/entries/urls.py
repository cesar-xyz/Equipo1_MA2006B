from rest_framework import routers

from .viewsets import EntryViewSet

router = routers.DefaultRouter()
router.register("entries", EntryViewSet)
