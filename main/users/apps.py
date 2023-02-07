from django.apps import AppConfig

# Configuración de la aplicación 'users'
class UsersConfig(AppConfig):
    # Tipo de campo automático por defecto
    default_auto_field = "django.db.models.BigAutoField"
    # Nombre de la aplicación
    name = "users"
