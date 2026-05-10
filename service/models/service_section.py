from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager

class ServiceSection(BaseModel):
    subtitle = models.CharField(max_length=255, help_text="Subtitle for the service section")
    title = models.CharField(max_length=255, help_text="Main title for the service section")
    description = models.TextField(help_text="Description of the service section")
    cta_title = models.CharField(max_length=255, help_text="Title for the call-to-action section")
    cta_description = models.TextField(help_text="Description for the call-to-action section")
    primary_button = models.CharField(max_length=255, help_text="Text for the primary button")
    secondary_button = models.CharField(max_length=255, help_text="Text for the secondary button")
    features_label = models.CharField(max_length=255, default="Key Features:", help_text="Label for the features section")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()
    
    class Meta:
        verbose_name = "Service Section"
        verbose_name_plural = "Service Sections"

    def __str__(self):
        return self.title
