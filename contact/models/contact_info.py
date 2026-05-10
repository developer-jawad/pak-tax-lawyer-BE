from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class ContactInfo(BaseModel):
    icon = models.CharField(
        max_length=255, help_text="Icon name (e.g., Phone, Email, LocationOn)"
    )
    title = models.CharField(
        max_length=255, help_text="Contact info title (e.g., Phone, Email)"
    )
    details = models.CharField(
        max_length=500, help_text="Contact details (e.g., phone number, email address)"
    )
    subtitle = models.CharField(max_length=255, help_text="Additional info or subtitle")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"
        ordering = ["id"]

    def __str__(self):
        return f"{self.title} - {self.details}"
