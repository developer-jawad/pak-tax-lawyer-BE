from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class BlogStatistic(BaseModel):
    number = models.CharField(max_length=255, help_text="The statistic number or value (e.g., 100+, 50K+)")
    label = models.CharField(max_length=255, help_text="The label describing the statistic (e.g., Articles Published)")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Blog Statistic"
        verbose_name_plural = "Blog Statistics"
        ordering = ['id']

    def __str__(self):
        return f"{self.number} - {self.label}"
