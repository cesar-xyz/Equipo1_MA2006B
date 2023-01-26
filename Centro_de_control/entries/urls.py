from rest_framework import routers

from entries.viewsets import EntryViewSet

router = routers.DefaultRouter()
router.register("entries", EntryViewSet)
