from django.contrib import admin

from .models import ControlCenter


@admin.register(ControlCenter)
class ControlCenterAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
