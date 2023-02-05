from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
User = settings.AUTH_USER_MODEL


class Certificate(models.Model):
    auditor = models.OneToOneField(
        "auditors.Auditor",
        verbose_name=_("auditor"),
        related_name="certificates",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        unique=True,
    )
    control_center = models.ForeignKey(
        "control_center.ControlCenter",
        verbose_name=_("control_center"),
        related_name=_("certificates"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    public_key = models.OneToOneField(
        "public_keys.PublicKey",
        verbose_name=_("public_key"),
        related_name="certificates",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_authorized = models.BooleanField(_("is_authorized"), default=True)
    expiring_date = models.DateTimeField(default=datetime.now() + timedelta(minutes=3), editable=False)


    def check_expiry(self):
        now = datetime.now(pytz.UTC)
        if self.expiring_date is not None and now >= self.expiring_date:
            self.is_authorized = False
            self.save()
            return False
        return True

    class Meta:
        verbose_name = _("certificate")
        verbose_name_plural = _("certificates")
