from django.contrib import admin

from .models import LeadSearch


@admin.register(LeadSearch)
class LeadSearchAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "niche",
        "location",
        "status",
        "created_by",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "niche",
        "location",
    )