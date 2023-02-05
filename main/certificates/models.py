from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class Certificate(Paranoid):
    auditor = models.ForeignKey(
        "auditors.Auditor",
        verbose_name=_("auditor"),
        related_name="certificates",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    control_center = models.ForeignKey(
        "control_center.ControlCenter",
        verbose_name=_("control_center"),
        related_name=_("certificates"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    public_key = models.ForeignKey(
        "public_keys.PublicKey",
        verbose_name=_("public_key"),
        related_name="certificates",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    expiring_date = models.CharField(_("expiring date"), max_length=128)

    class Meta:
        verbose_name = _("certificate")
        verbose_name_plural = _("certificates")
