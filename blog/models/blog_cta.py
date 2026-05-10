from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class BlogCTA(BaseModel):
    button_text = models.CharField(max_length=100, help_text="CTA button text")
    button_link = models.CharField(max_length=500, help_text="CTA button link")
    is_blog_section = models.BooleanField(default=True, help_text="Whether this CTA is for the blog section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Blog CTA"
        verbose_name_plural = "Blog CTAs"

    def __str__(self):
        return self.button_text
