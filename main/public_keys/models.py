from django.db import models
from django.utils.translation import gettext as _
from django_extensions.validators import HexValidator
# Importar la biblioteca Paranoid
from paranoid_model.models import Paranoid


# Importar la clase HexValidator para validar los datos del campo hexadecimal

# Se crea una clase propia llamada HexadecimalField que hereda de la clase models.CharField
class HexadecimalField(models.CharField):
    def __init__(self, *args, **kwargs):
        # Llamar al constructor de la clase padre
        super(HexadecimalField, self).__init__(*args, **kwargs)


# Se crea un modelo llamado PublicKey que hereda de Paranoid
class PublicKey(Paranoid):
    # Campo que almacena el algoritmo que utiliza para la generación de la llave pública
    algorithm = models.CharField(_("algorithm"), max_length=256, blank=True, null=True)

    # Campo que almacenará la clave pública en formato hexadecimal
    key = HexadecimalField(
        _("public key"), max_length=128, validators=[HexValidator(length=128)]
    )

    # Clase Meta que especifica el nombre y el nombre plural del modelo en singular y plural
    class Meta:
        verbose_name = _("public key")
        verbose_name_plural = _("public keys")

    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"Public key: {self.pk}"
