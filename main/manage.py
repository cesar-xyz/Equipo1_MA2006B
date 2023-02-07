#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Establecemos el módulo de configuración de Django por defecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Importamos la función `execute_from_command_line` desde `django.core.management`
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Mostramos un mensaje de error en caso de que Django no esté instalado o no esté disponible en el entorno de Python
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecutamos la línea de comando proporcionada
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
