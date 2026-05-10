from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class TestimonialCTA(BaseModel):
    title = models.CharField(max_length=255, help_text="CTA title")
    description = models.TextField(help_text="CTA description")
    button_text = models.CharField(
        max_length=100, blank=True, null=True, help_text="Button text"
    )
    button_link = models.CharField(
        max_length=255, blank=True, null=True, help_text="Button link"
    )
    is_testimonial_section = models.BooleanField(
        default=True, help_text="Whether this CTA belongs to testimonial section"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Testimonial CTA"
        verbose_name_plural = "Testimonial CTAs"

    def __str__(self):
        return self.title
