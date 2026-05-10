from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager


class TeamMember(BaseModel):
    name = models.CharField(max_length=255, help_text="Full name of the team member")
    position = models.CharField(max_length=255, help_text="Job title or position")
    specialization = models.CharField(max_length=255, help_text="Area of specialization")
    avatar = models.ImageField(upload_to='team_members/', blank=True, null=True, help_text="Team member photo")
    bio = models.TextField(help_text="Short biography of the team member")
    credentials = models.JSONField(default=list, help_text="List of credentials as JSON array")
    email = models.EmailField(blank=True, null=True, help_text="Email address")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Phone number")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn profile URL")
    featured = models.BooleanField(default=False, help_text="Whether this member is featured")
    featured_label = models.CharField(max_length=50, blank=True, null=True, help_text="Label for featured members")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['-featured', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"
