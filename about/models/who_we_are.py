from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class WhoWeAre(BaseModel):
    subtitle = models.CharField(max_length=255, help_text="Subtitle for who we are section")
    title = models.CharField(max_length=255, help_text="Main title for who we are section")
    paragraphs = models.JSONField(default=list, help_text="Paragraphs as JSON array")
    image_overlay_title = models.CharField(max_length=255, help_text="Image overlay title", blank=True, null=True)
    image_overlay_description = models.CharField(max_length=255, help_text="Image overlay description", blank=True, null=True)

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Who We Are"
        verbose_name_plural = "Who We Are"

    def __str__(self):
        return self.title
