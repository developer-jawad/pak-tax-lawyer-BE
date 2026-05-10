from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager

class ServiceBenefit(BaseModel):
    icon = models.CharField(max_length=255, help_text="Icon name or identifier for the benefit")
    text = models.CharField(max_length=255, help_text="Text describing the benefit")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()
    class Meta:
        verbose_name = "Service Benefit"
        verbose_name_plural = "Service Benefits"
        ordering = ['id']

    def __str__(self):
        return self.text
