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

    class Meta:
        verbose_name = _("public key")
        verbose_name_plural = _("public keys")

    def __str__(self):
        return f"{self.pk}: {self.key}"
