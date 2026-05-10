from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class VideoCTA(BaseModel):
    title = models.CharField(max_length=255, help_text="CTA title")
    description = models.TextField(help_text="CTA description")
    video_count = models.CharField(max_length=50, help_text="Video count (e.g., 100+)")
    video_count_label = models.CharField(
        max_length=255, help_text="Video count label (e.g., Educational Videos)"
    )
    button_text = models.CharField(max_length=255, help_text="Button text")
    button_link = models.CharField(max_length=255, help_text="Button link")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Video CTA"
        verbose_name_plural = "Video CTAs"

    def __str__(self):
        return self.title
