from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

# Manager personalizado para el modelo de usuario
class CustomUserManager(BaseUserManager):
    """
    Manager de modelo de usuario personalizado donde el correo electrónico es el identificador único
    para la autenticación en lugar de los nombres de usuario.
    """

    def create_user(self, email, password, **extra_fields):
        # Verificar que el usuario proporcione un correo electrónico
        if not email:
            raise ValueError(_("Los usuarios deben tener una dirección de correo electrónico"))
        # Normalizar el correo electrónico del usuario
        email = self.normalize_email(email)
        # Crear un nuevo usuario
        user = self.model(email=email, **extra_fields)
        # Establecer la contraseña para el usuario
        user.set_password(password)
        # Guardar el usuario en la base de datos
        user.save()
        # Devolver el usuario creado
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Establecer valores por defecto para los campos is_staff y is_superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Verificar que el usuario tenga is_staff=True
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("El superusuario debe tener is_staff=True."))
        # Verificar que el usuario tenga is_superuser=True
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("El superusuario debe tener is_superuser=True."))
        # Crear un superusuario
        return self.create_user(email, password, **extra_fields)
