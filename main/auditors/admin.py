from django.contrib import admin

from .models import Auditor


@admin.register(Auditor)
class AuditorAdmin(admin.ModelAdmin):
    list_display = ["name", "mac_address", "is_authorized"]
    search_fields = ["name", "mac_address", "is_authorized"]
