from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class FooterQuickLink(BaseModel):
    label = models.CharField(max_length=255, help_text="Link label")
    url = models.CharField(max_length=500, help_text="Link URL")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Footer Quick Link"
        verbose_name_plural = "Footer Quick Links"
        ordering = ['id']

    def __str__(self):
        return self.label
