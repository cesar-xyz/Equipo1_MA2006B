from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class Auditor(Paranoid):
    name = models.CharField(_("name"), max_length=128)
    mac_address = models.CharField(_("mac address"), max_length=256)
    class Meta:
        verbose_name = _("auditor")
        verbose_name_plural = _("auditors")

    def __str__(self):
        return f"Auditor: {self.name}"
