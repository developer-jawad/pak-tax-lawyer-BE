from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class TestimonialSection(BaseModel):
    subtitle = models.CharField(
        max_length=255, help_text="Subtitle for the testimonial section"
    )
    title = models.CharField(
        max_length=255, help_text="Main title for the testimonial section"
    )
    description = models.TextField(help_text="Description of the testimonial section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Testimonial Section"
        verbose_name_plural = "Testimonial Sections"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="home_testimsect_active"),
        ]

    def __str__(self):
        return self.title
