from django.contrib import admin

from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ["auditor", "is_authorized", "control_center", "expiring_date"]
    search_fields = ["auditor", "control_center", "expiring_date"]
