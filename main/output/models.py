from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class Output(Paranoid):
    MESSAGE_CHOISE = (
        ("1", "Upload"),
        ("2", "Shutdown"),
        ("3", "Disconnect"),
    )
    out_auditor = models.ForeignKey(
        "auditors.Auditor",
        verbose_name=_("out_auditor"),
        related_name="out_auditors",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    message = models.CharField(_("message"), choices=MESSAGE_CHOISE, max_length=64, blank=True, null=True)
    received = models.BooleanField(_("received"), default=False, editable=False)

    class Meta:
        verbose_name = _("output")
        verbose_name_plural = _("outputs")
