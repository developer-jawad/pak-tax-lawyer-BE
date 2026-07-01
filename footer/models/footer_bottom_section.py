from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class FooterBottomSection(BaseModel):
    copyright = models.TextField(
        help_text="Copyright text (use {year} placeholder for year)"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Footer Bottom Section"
        verbose_name_plural = "Footer Bottom Sections"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="footer_bottomsect_active"),
        ]

    def __str__(self):
        return self.copyright[:50]
