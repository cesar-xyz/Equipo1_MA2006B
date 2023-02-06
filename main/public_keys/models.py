from django.db import models
from django.utils.translation import gettext as _
from django_extensions.validators import HexValidator

# from djangoHexadecimal.fields import HexadecimalField
from paranoid_model.models import Paranoid


class HexadecimalField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(HexadecimalField, self).__init__(*args, **kwargs)


class PublicKey(Paranoid):
    key = HexadecimalField(
        _("public key"), max_length=512, validators=[HexValidator(length=256)]
    )
    prime_p = models.CharField(
        _("prime number p"), max_length=256, blank=True, null=True
    )
    curve_a = models.CharField(_("curve a"), max_length=256, blank=True, null=True)
    curve_b = models.CharField(_("curve b"), max_length=256, blank=True, null=True)
    order_q = models.CharField(_("order q"), max_length=256, blank=True, null=True)
    generator = models.CharField(
        _("generator A"), max_length=256, blank=True, null=True
    )
    cor_ver = models.CharField(
        _("verification coordinate B"), max_length=256, blank=True, null=True
    )

    class Meta:
        verbose_name = _("public key")
        verbose_name_plural = _("public keys")

    def __str__(self):
        return f"{self.pk}: {self.key}"
