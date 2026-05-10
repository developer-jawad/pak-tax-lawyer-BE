from django.core.validators import URLValidator
from django.db import models

from common.models import BaseModel


class HeroSection(BaseModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=500, validators=[URLValidator()])
    background_gradient = models.CharField(
        max_length=500,
        help_text="CSS gradient string (e.g., 'linear-gradient(135deg, #000000 0%, #333333 100%)')",
    )
    background_image_url = models.URLField(
        max_length=1000,
        blank=True,
        null=True,
        help_text="External URL for background image",
    )
    background_image = models.ImageField(
        upload_to="hero_sections/",
        blank=True,
        null=True,
        help_text="Upload background image (optional if using external URL)",
    )

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_background_image(self):
        if self.background_image:
            return self.background_image.url
        return self.background_image_url
