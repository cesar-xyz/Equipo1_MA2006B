from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

# Creamos una clase que hereda de AbstractUser de Django
class User(AbstractUser):
    # Sobrescribimos el campo username y lo ponemos a None
    username = None
    # Agregamos un campo de correo electrónico único
    email = models.EmailField(_("email address"), unique=True)

    # Definimos el campo de correo electrónico como el campo único de identificación
    USERNAME_FIELD = "email"
    # Definimos los campos requeridos como una tupla vacía
    REQUIRED_FIELDS = ()

    # Definimos el administrador de objetos como CustomUserManager
    objects = CustomUserManager()

    # Definimos las opciones de Meta para el modelo
    class Meta:
        # Nombre para un solo usuario
        verbose_name = "user"
        # Nombre para varios usuarios
        verbose_name_plural = "users"

    # Sobrescribimos el método __str__ para representar al usuario como una cadena de correo electrónico
    def __str__(self):
        return self.email
