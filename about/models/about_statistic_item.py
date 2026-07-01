from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class AboutStatisticItem(BaseModel):
    icon = models.CharField(
        max_length=255, help_text="Icon name (e.g., People, TrendingUp)"
    )
    value = models.CharField(
        max_length=255, help_text="Statistic value (e.g., 500+, 10+)"
    )
    label = models.CharField(
        max_length=255, help_text="Statistic label (e.g., Happy Clients)"
    )
    color = models.CharField(
        max_length=50, default="#EE1C27", help_text="Color for the statistic"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Statistic Item"
        verbose_name_plural = "About Statistic Items"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="about_statitem_active"),
        ]

    def __str__(self):
        return f"{self.value} - {self.label}"
