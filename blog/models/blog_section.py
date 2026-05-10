from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class BlogSection(BaseModel):
    subtitle = models.CharField(max_length=255, help_text="Subtitle for the blog section")
    title = models.CharField(max_length=255, help_text="Main title for the blog section")
    description = models.TextField(help_text="Description of the blog section")
    categories = models.JSONField(default=list, help_text="Categories as integer array")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Sections"

    def __str__(self):
        return self.title
