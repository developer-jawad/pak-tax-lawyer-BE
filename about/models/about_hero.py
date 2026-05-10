from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class AboutHero(BaseModel):
    title = models.CharField(
        max_length=255, help_text="Title for the about hero section"
    )
    subtitle = models.CharField(
        max_length=255, help_text="Subtitle for the about hero section"
    )
    description = models.TextField(help_text="Description of the about hero section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Hero"
        verbose_name_plural = "About Heroes"

    def __str__(self):
        return self.title
