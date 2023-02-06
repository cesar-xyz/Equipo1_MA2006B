"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from users.urls import router as user_router
from entries.urls import router as entry_router
from public_keys.urls import router as public_keys_router
from auditors.urls import router as auditors_router
from control_center.urls import router as control_center_router
from certificates.urls import router as certificates_router
from output.urls import router as outputs_router

router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(entry_router.registry)
router.registry.extend(outputs_router.registry)
router.registry.extend(public_keys_router.registry)
router.registry.extend(auditors_router.registry)
router.registry.extend(control_center_router.registry)
router.registry.extend(certificates_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/v1/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
]
