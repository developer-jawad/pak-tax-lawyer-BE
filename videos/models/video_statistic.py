from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class VideoStatistic(BaseModel):
    number = models.CharField(
        max_length=255, help_text="The statistic number or value (e.g., 50+, 5K+)"
    )
    label = models.CharField(
        max_length=255,
        help_text="The label describing the statistic (e.g., Video Tutorials)",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Video Statistic"
        verbose_name_plural = "Video Statistics"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="video_stat_active"),
        ]

    def __str__(self):
        return f"{self.number} - {self.label}"
