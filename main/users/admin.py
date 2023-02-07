from .models import User

# Registra CustomUserAdmin como el panel de administración para el modelo User
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # Campos a mostrar en la vista de lista de objetos User
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )

    # Opciones de filtro disponibles en la barra lateral
    list_filter = ("is_active", "is_staff", "is_superuser")

    # Agrupación de campos en la página de edición de usuario
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Permisos",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas", {"fields": ("last_login", "date_joined")}),
    )

    # Agrupación de campos en la página de creación de usuario
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    # Campos para buscar un usuario
    search_fields = ("email",)

    # Orden por defecto para objetos User en la vista de lista
    ordering = ("email",)
