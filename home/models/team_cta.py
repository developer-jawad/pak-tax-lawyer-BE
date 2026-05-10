from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class TeamCTA(BaseModel):
    title = models.CharField(max_length=255, help_text="CTA title")
    description = models.TextField(help_text="CTA description")
    email = models.EmailField(help_text="Contact email for the CTA")
    is_team_section = models.BooleanField(
        default=True, help_text="Whether this CTA is for the team section"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Team CTA"
        verbose_name_plural = "Team CTAs"

    def __str__(self):
        return self.title
