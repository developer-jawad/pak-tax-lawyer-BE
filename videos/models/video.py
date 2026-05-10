from django.db import models
from common.models import BaseModel
from common.managers import ActiveObjectsManager
from common.constants import BLOG_CATEGORIES, BLOG_CATEGORY_CHOICES


class Video(BaseModel):
    title = models.CharField(max_length=255, help_text="Video title")
    description = models.TextField(help_text="Video description")
    thumbnail = models.URLField(max_length=1000, blank=True, null=True, help_text="Thumbnail image URL")
    duration = models.CharField(max_length=50, help_text="Video duration (e.g., 12:45)")
    views = models.CharField(max_length=50, blank=True, null=True, help_text="View count (e.g., 15.2K)")
    category = models.IntegerField(choices=BLOG_CATEGORY_CHOICES, default=BLOG_CATEGORIES.all, help_text="Video category")
    video_url = models.URLField(max_length=1000, help_text="YouTube video URL or embed URL")
    trending = models.BooleanField(default=False, help_text="Whether the video is trending")
    new = models.BooleanField(default=False, help_text="Whether the video is new")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-trending', '-new', '-created_at']

    def __str__(self):
        return self.title
