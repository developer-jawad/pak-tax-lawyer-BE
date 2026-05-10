from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


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

    def __str__(self):
        return self.title
