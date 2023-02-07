from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid

# Clase Output que hereda de Paranoid
class Output(Paranoid):
    # Tupla con opciones para el campo message
    MESSAGE_CHOISE = (
        ("1", "Upload"),
        ("2", "Shutdown"),
        ("3", "Disconnect"),
    )

    # Campo de tipo ForeignKey a la tabla "auditors.Auditor", con nombre de la relación "out_auditor"
    out_auditor = models.ForeignKey(
        "auditors.Auditor",
        verbose_name=_("out_auditor"),
        related_name="out_auditors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # Campo de tipo CharField con opciones MESSAGE_CHOISE
    message = models.CharField(_("message"), choices=MESSAGE_CHOISE, max_length=64, blank=True, null=True)

    # Campo de tipo BooleanField con valor por defecto False y sin permisos de edición
    received = models.BooleanField(_("received"), default=False, editable=False)

    # Clase Meta con información para la presentación en el panel de administración
    class Meta:
        verbose_name = _("output")
        verbose_name_plural = _("outputs")
