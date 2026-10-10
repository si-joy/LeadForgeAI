from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "business_name",
        "category",
        "country",
        "ai_score",
        "status",
        "verification_status",
        "created_at",
    )

    list_filter = (
        "status",
        "verification_status",
        "country",
        "created_at",
    )

    search_fields = (
        "business_name",
        "domain",
        "public_email",
        "public_phone",
    )