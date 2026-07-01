from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class AboutStatistic(BaseModel):
    number = models.CharField(
        max_length=255, help_text="The statistic number or value (e.g., 500+, 10+)"
    )
    label = models.CharField(
        max_length=255,
        help_text="The label describing the statistic (e.g., Happy Clients)",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Statistic"
        verbose_name_plural = "About Statistics"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="about_stat_active"),
        ]

    def __str__(self):
        return f"{self.number} - {self.label}"
