from django.contrib import admin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'auditor', 'is_producing', 'quantity')
    search_fields = ('id', 'date')
