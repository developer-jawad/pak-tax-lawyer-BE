from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class Testimonial(BaseModel):
    name = models.CharField(max_length=255, help_text="Full name of the client")
    role = models.CharField(max_length=255, help_text="Job title or role")
    company = models.CharField(max_length=255, help_text="Company name")
    avatar = models.CharField(max_length=10, help_text="Avatar initials (e.g., 'AH' for Ahmed Hassan)")
    rating = models.IntegerField(default=5, help_text="Rating out of 5")
    testimonial = models.TextField(help_text="Client testimonial text")
    location = models.CharField(max_length=255, help_text="Client location")
    featured = models.BooleanField(default=False, help_text="Whether this testimonial is featured")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-featured', 'id']

    def __str__(self):
        return f"{self.name} - {self.company}"
