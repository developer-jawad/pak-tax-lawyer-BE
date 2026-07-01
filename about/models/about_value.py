from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class AboutValue(BaseModel):
    icon = models.CharField(
        max_length=255, help_text="Icon name (e.g., Verified, WorkspacePremium)"
    )
    title = models.CharField(max_length=255, help_text="Value title")
    description = models.TextField(help_text="Value description")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Value"
        verbose_name_plural = "About Values"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="about_value_active"),
        ]

    def __str__(self):
        return self.title
