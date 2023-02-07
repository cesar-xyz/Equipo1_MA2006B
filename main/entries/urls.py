from rest_framework import routers

from .viewsets import EntryViewSet

# Create a router object
router = routers.DefaultRouter()

# Register the EntryViewSet with the router object, using the "entries" URL path prefix
router.register("entries", EntryViewSet)

