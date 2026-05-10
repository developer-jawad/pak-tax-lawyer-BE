from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class FooterBrand(BaseModel):
    name = models.CharField(max_length=255, help_text="Brand name")
    description = models.TextField(help_text="Brand description")
    logo_alt = models.CharField(max_length=255, help_text="Logo alt text")
    follow_us = models.CharField(
        max_length=255, default="Follow Us", help_text="Follow us text"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Footer Brand"
        verbose_name_plural = "Footer Brands"

    def __str__(self):
        return self.name
