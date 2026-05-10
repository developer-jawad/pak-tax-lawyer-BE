from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ContactHero(BaseModel):
    title = models.CharField(
        max_length=255, help_text="Title for the contact hero section"
    )
    subtitle = models.CharField(
        max_length=255, help_text="Subtitle for the contact hero section"
    )
    description = models.TextField(help_text="Description of the contact hero section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Contact Hero"
        verbose_name_plural = "Contact Heroes"

    def __str__(self):
        return self.title
