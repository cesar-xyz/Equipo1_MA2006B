from django.contrib import admin

from .models import Output


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ['out_auditor', 'message', 'received']
    search_fields = ['out_auditor', 'message', 'received']
