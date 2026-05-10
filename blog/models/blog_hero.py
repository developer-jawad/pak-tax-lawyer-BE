from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class BlogHero(BaseModel):
    title = models.CharField(max_length=255, help_text="Title for the blog hero section")
    subtitle = models.CharField(max_length=255, help_text="Subtitle for the blog hero section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Blog Hero"
        verbose_name_plural = "Blog Heroes"

    def __str__(self):
        return self.title
