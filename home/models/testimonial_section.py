from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class TestimonialSection(BaseModel):
    subtitle = models.CharField(max_length=255, help_text="Subtitle for the testimonial section")
    title = models.CharField(max_length=255, help_text="Main title for the testimonial section")
    description = models.TextField(help_text="Description of the testimonial section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Testimonial Section"
        verbose_name_plural = "Testimonial Sections"

    def __str__(self):
        return self.title
