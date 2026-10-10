from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "LeadForge",
            {
                "fields": (
                    "role",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "LeadForge",
            {
                "fields": (
                    "email",
                    "role",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "role",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
    )