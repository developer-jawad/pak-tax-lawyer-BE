from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class FooterContact(BaseModel):
    title = models.CharField(max_length=255, default="Contact Us", help_text="Contact section title")
    address_label = models.CharField(max_length=255, default="Office Address", help_text="Address label")
    address_value = models.TextField(help_text="Office address")
    phone_label = models.CharField(max_length=255, default="Phone", help_text="Phone label")
    phone_value = models.CharField(max_length=255, help_text="Phone number")
    email_label = models.CharField(max_length=255, default="Email", help_text="Email label")
    email_value = models.EmailField(max_length=255, help_text="Email address")
    business_hours_label = models.CharField(max_length=255, default="Business Hours", help_text="Business hours label")
    business_hours_value = models.CharField(max_length=255, help_text="Business hours")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Footer Contact"
        verbose_name_plural = "Footer Contact"

    def __str__(self):
        return self.title
