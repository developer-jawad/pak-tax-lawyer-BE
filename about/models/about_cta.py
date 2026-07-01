from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class AboutCTA(BaseModel):
    title = models.CharField(max_length=255, help_text="CTA title")
    description = models.TextField(help_text="CTA description")
    phone = models.CharField(max_length=50, help_text="Phone number")
    email = models.EmailField(help_text="Email address")
    button_text = models.CharField(max_length=255, help_text="Button text")
    button_link = models.CharField(max_length=255, help_text="Button link")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "About CTA"
        verbose_name_plural = "About CTAs"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="about_cta_active"),
        ]

    def __str__(self):
        return self.title
