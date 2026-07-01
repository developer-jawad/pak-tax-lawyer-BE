from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ServiceCTA(BaseModel):
    is_service_section = models.BooleanField(
        default=False, help_text="Whether this call-to-action is for a service section"
    )
    title = models.CharField(
        max_length=255, help_text="Title for the call-to-action section"
    )
    description = models.TextField(
        help_text="Description for the call-to-action section"
    )
    button_text = models.CharField(
        max_length=255, help_text="Text to display on the call-to-action button"
    )
    button_link = models.URLField(help_text="URL link for the call-to-action button")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Service CTA"
        verbose_name_plural = "Service CTAs"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="service_cta_active"),
        ]

    def __str__(self):
        return self.title
