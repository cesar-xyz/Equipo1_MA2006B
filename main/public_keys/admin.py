from django.contrib import admin

from .models import PublicKey


@admin.register(PublicKey)
class PublicKeyAdmin(admin.ModelAdmin):
    list_display = [
        "key",
        "prime_p",
        "curve_a",
        "curve_b",
        "order_q",
        "generator",
        "cor_ver",
    ]
    search_fields = [
        "key",
        "prime_p",
        "curve_a",
        "curve_b",
        "order_q",
        "generator",
        "cor_ver",
    ]
