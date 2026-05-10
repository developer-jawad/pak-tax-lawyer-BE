from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class VideoHero(BaseModel):
    title = models.CharField(
        max_length=255, help_text="Title for the video hero section"
    )
    subtitle = models.CharField(
        max_length=255, help_text="Subtitle for the video hero section"
    )
    description = models.TextField(help_text="Description of the video hero section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Video Hero"
        verbose_name_plural = "Video Heroes"

    def __str__(self):
        return self.title
