from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class ContactCTA(BaseModel):
    icon = models.CharField(max_length=255, help_text="Icon name (e.g., CheckCircle)")
    title = models.CharField(max_length=255, help_text="CTA title")
    description = models.TextField(help_text="CTA description")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Contact CTA"
        verbose_name_plural = "Contact CTAs"

    def __str__(self):
        return self.title
