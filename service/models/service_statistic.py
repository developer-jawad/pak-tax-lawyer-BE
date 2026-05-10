from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ServiceStatistic(BaseModel):
    number = models.CharField(
        max_length=255, help_text="The statistic number or value (e.g., 500+, 15+)"
    )
    label = models.CharField(
        max_length=255,
        help_text="The label describing the statistic (e.g., Clients Served)",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Service Statistic"
        verbose_name_plural = "Service Statistics"
        ordering = ["id"]

    def __str__(self):
        return f"{self.number} - {self.label}"
