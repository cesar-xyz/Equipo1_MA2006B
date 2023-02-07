from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid

# Creamos una clase de modelo Entry que hereda de Paranoid
class Entry(Paranoid):
    # Un campo llamado "auditor" que hace referencia a un registro en la tabla "Auditor"
    auditor = models.ForeignKey(
        "auditors.Auditor",
        verbose_name=_("auditor"),
        related_name="auditors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # Un campo de tipo cadena llamado "date"
    date = models.CharField(_("date"), max_length=64, blank=True)
    # Un campo booleano llamado "is_producing"
    is_producing = models.BooleanField(_("is producing?"), blank=True, null=True)
    # Un campo decimal llamado "quantity"
    quantity = models.DecimalField(
        _("quantity"), decimal_places=2, max_digits=6, blank=True, null=True
    )
    # Un campo de tipo cadena llamado "mac_emisor"
    mac_emisor = models.CharField(_("mac_emisor"), max_length=64, blank=True, null=True)
    # Un campo de tipo cadena llamado "ip_receptor"
    ip_receptor = models.CharField(
        _("ip_receptor"), max_length=64, blank=True, null=True
    )
    # Un campo llamado "public_key" que hace referencia a un registro en la tabla "PublicKey"
    public_key = models.ForeignKey(
        "public_keys.PublicKey",
        verbose_name=_("public_key"),
        related_name="public_keys",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # Metadatos para la clase Entry
    class Meta:
        verbose_name = _("entry")
        verbose_name_plural = _("entries")

    # Función para representar un objeto Entry como una cadena
    def __str__(self):
        if self.is_producing:
            return f"Cantidad de Producción: {self.quantity}"
        return f"Cantidad de Consumo: {self.quantity}"
