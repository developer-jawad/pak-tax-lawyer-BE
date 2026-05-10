from django.contrib.postgres.fields import ArrayField
from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class Service(BaseModel):
    service_section = models.ForeignKey(
        "ServiceSection",
        on_delete=models.CASCADE,
        related_name="services",
        null=True,
        blank=True,
        help_text="The service section this service belongs to",
    )
    title = models.CharField(max_length=255, help_text="The title of the service")
    description = models.TextField(help_text="Detailed description of the service")
    icon = models.CharField(
        max_length=255, help_text="Icon name or identifier for the service"
    )
    color = models.CharField(
        max_length=255, help_text="Color code for the service (e.g., #EE1C27)"
    )
    button_text = models.CharField(
        max_length=255, help_text="Text to display on the service button"
    )
    badge = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Badge text to highlight the service",
    )
    popular = models.BooleanField(default=False, help_text="Mark as popular service")
    features = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        default=list,
        help_text="List of service features",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["id"]

    def __str__(self):
        return self.title
