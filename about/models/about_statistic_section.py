from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class AboutStatisticSection(BaseModel):
    title = models.CharField(
        max_length=255, help_text="Title for the statistics section"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Statistic Section"
        verbose_name_plural = "About Statistic Sections"

    def __str__(self):
        return self.title
