from django.conf import settings
from django.db import models

from searches.models import LeadSearch


class Lead(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEWING = "reviewing", "Reviewing"
        QUALIFIED = "qualified", "Qualified"
        CONTACTED = "contacted", "Contacted"
        WON = "won", "Won"
        REJECTED = "rejected", "Rejected"

    class VerificationStatus(models.TextChoices):
        UNVERIFIED = "unverified", "Unverified"
        VERIFIED = "verified", "Verified"
        FAILED = "failed", "Failed"

    search = models.ForeignKey(
        LeadSearch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
    )

    business_name = models.CharField(max_length=255)

    website = models.URLField(
        max_length=500,
        blank=True,
    )

    domain = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )

    category = models.CharField(
        max_length=150,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    address = models.TextField(blank=True)

    public_email = models.EmailField(
        blank=True,
    )

    public_phone = models.CharField(
        max_length=50,
        blank=True,
    )

    source_name = models.CharField(
        max_length=100,
        blank=True,
    )

    source_url = models.URLField(
        max_length=1000,
        blank=True,
    )

    ai_score = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    ai_summary = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        db_index=True,
    )

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.UNVERIFIED,
    )

    notes = models.TextField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="leads",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["created_by", "domain"],
                name="unique_lead_domain_per_user",
                condition=~models.Q(domain=""),
            )
        ]

        indexes = [
            models.Index(fields=["created_by", "status"]),
            models.Index(fields=["country", "city"]),
            models.Index(fields=["ai_score"]),
        ]

    def __str__(self):
        return self.business_name