from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ServiceHero(BaseModel):
    title = models.CharField(
        max_length=255, help_text="Main title for the hero section"
    )
    subtitle = models.TextField(help_text="Subtitle or tagline for the hero section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Service Hero"
        verbose_name_plural = "Service Heroes"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="service_hero_active"),
        ]

    def __str__(self):
        return self.title
