from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class ContactForm(BaseModel):
    title = models.CharField(max_length=255, help_text="Form title")
    description = models.TextField(help_text="Form description")
    name_label = models.CharField(max_length=255, default="Full Name", help_text="Name field label")
    email_label = models.CharField(max_length=255, default="Email Address", help_text="Email field label")
    phone_label = models.CharField(max_length=255, default="Phone Number", help_text="Phone field label")
    subject_label = models.CharField(max_length=255, default="Subject", help_text="Subject field label")
    message_label = models.CharField(max_length=255, default="Message", help_text="Message field label")
    submit_button_text = models.CharField(max_length=255, default="Send Message", help_text="Submit button text")
    loading_text = models.CharField(max_length=255, default="Sending...", help_text="Loading text")
    success_message = models.TextField(help_text="Success message after form submission")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"

    def __str__(self):
        return self.title
