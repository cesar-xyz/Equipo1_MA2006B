from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class Entry(Paranoid):
    auditor = models.ForeignKey(
        "auditors.Auditor",
        verbose_name=_("auditor"),
        related_name="auditors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.CharField(_("date"), max_length=64, blank=True)
    is_producing = models.BooleanField(_("is producing?"), blank=True, null=True)
    quantity = models.DecimalField(
        _("quantity"), decimal_places=2, max_digits=6, blank=True, null=True
    )
    mac_emisor = models.CharField(_("mac_emisor"), max_length=64, blank=True, null=True)
    ip_receptor = models.CharField(
        _("ip_receptor"), max_length=64, blank=True, null=True
    )
    public_key = models.ForeignKey(
        "public_keys.PublicKey",
        verbose_name=_("public_key"),
        related_name="public_keys",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("entry")
        verbose_name_plural = _("entries")

    def __str__(self):
        if self.is_producing:
            return f"Cantidad de Producción: {self.quantity}"
        return f"Cantidad de Consumo: {self.quantity}"
