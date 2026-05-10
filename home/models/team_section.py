from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class TeamSection(BaseModel):
    subtitle = models.CharField(max_length=255, help_text="Subtitle for the team section")
    title = models.CharField(max_length=255, help_text="Main title for the team section")
    description = models.TextField(help_text="Description of the team section")
    credentials_label = models.CharField(max_length=100, default="Credentials:", help_text="Label for credentials field")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Team Section"
        verbose_name_plural = "Team Sections"

    def __str__(self):
        return self.title
