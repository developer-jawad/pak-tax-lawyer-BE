from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class FooterServiceLink(BaseModel):
    label = models.CharField(max_length=255, help_text="Link label")
    url = models.CharField(max_length=500, help_text="Link URL")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Footer Service Link"
        verbose_name_plural = "Footer Service Links"
        ordering = ['id']

    def __str__(self):
        return self.label
