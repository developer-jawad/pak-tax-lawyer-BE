from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ContactMap(BaseModel):
    title = models.CharField(max_length=255, help_text="Map section title")
    iframe_url = models.URLField(max_length=1000, help_text="Google Maps iframe URL")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Contact Map"
        verbose_name_plural = "Contact Maps"

    def __str__(self):
        return self.title
