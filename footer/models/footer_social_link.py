from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class FooterSocialLink(BaseModel):
    platform = models.CharField(
        max_length=255, help_text="Platform name (e.g., Facebook, Instagram)"
    )
    url = models.URLField(max_length=1000, help_text="Platform URL")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Footer Social Link"
        verbose_name_plural = "Footer Social Links"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="footer_sociallink_active"),
        ]

    def __str__(self):
        return f"{self.platform}"
