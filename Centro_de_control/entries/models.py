from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class Entry(Paranoid):
    auditor = models.CharField(_("auditor"), max_length=128, blank=True)
    date = models.CharField(_("date"), max_length=64, blank=True)
    is_producing = models.BooleanField(_("is producing?"), blank=True, null=True)
    quantity = models.DecimalField(_(""), decimal_places=2, max_digits=6, blank=True, null=True)

    class Meta:
        verbose_name = _("entry")
        verbose_name_plural = _("entries")

    def __str__(self):
        if self.is_producing:
            return f"Cantidad de Producción: {self.quantity}"
        return f"Cantidad de Consumo: {self.quantity}"
