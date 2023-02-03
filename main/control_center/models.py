from django.db import models
from django.utils.translation import gettext as _
from paranoid_model.models import Paranoid


class ControlCenter(Paranoid):
    name = models.CharField(_("name"), max_length=256)
    domain = models.CharField(_("domain url"), max_length=512)

    class Meta:
        verbose_name = _("control_center")
        verbose_name_plural = _("control_centers")

    def __str__(self):
        return f"Control Center: {self.name}"
