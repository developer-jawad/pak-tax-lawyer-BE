from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ContactStatistic(BaseModel):
    icon = models.CharField(
        max_length=255, help_text="Icon name (e.g., Schedule, Support)"
    )
    value = models.CharField(
        max_length=255, help_text="The statistic value (e.g., 24h, 10+)"
    )
    label = models.CharField(
        max_length=255,
        help_text="The label describing the statistic (e.g., Response Time)",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Contact Statistic"
        verbose_name_plural = "Contact Statistics"
        ordering = ["id"]

    def __str__(self):
        return f"{self.value} - {self.label}"
