from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ServiceSection(BaseModel):
    subtitle = models.CharField(
        max_length=255, help_text="Subtitle for the service section"
    )
    title = models.CharField(
        max_length=255, help_text="Main title for the service section"
    )
    description = models.TextField(help_text="Description of the service section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Service Section"
        verbose_name_plural = "Service Sections"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="service_sect_active"),
        ]

    def __str__(self):
        return self.title
