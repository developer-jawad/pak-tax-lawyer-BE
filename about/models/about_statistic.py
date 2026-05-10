from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class AboutStatistic(BaseModel):
    number = models.CharField(max_length=255, help_text="The statistic number or value (e.g., 500+, 10+)")
    label = models.CharField(max_length=255, help_text="The label describing the statistic (e.g., Happy Clients)")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Statistic"
        verbose_name_plural = "About Statistics"
        ordering = ['id']

    def __str__(self):
        return f"{self.number} - {self.label}"
