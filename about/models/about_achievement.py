from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class AboutAchievement(BaseModel):
    icon = models.CharField(max_length=255, help_text="Icon name (e.g., EmojiEvents, WorkspacePremium)")
    title = models.CharField(max_length=255, help_text="Achievement title")
    description = models.TextField(help_text="Achievement description")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About Achievement"
        verbose_name_plural = "About Achievements"
        ordering = ['id']

    def __str__(self):
        return self.title
