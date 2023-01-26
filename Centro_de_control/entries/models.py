from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class Entry(Paranoid):
    is_producing = models.BooleanField(_("is producing?"), blank=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=6, blank=True)

    class Meta:
        verbose_name = _("entry")
        verbose_name_plural = _("entries")

    def __str__(self):
        if self.is_producing:
            return f"Cantidad de Producción: {self.quantity}"
        return f"Cantidad de Consumo: {self.quantity}"
