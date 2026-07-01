from django.db import models

from common.managers import ActiveObjectsManager
from common.models import BaseModel


class VideoSection(BaseModel):
    title = models.CharField(max_length=255, help_text="Title for the video section")
    subtitle = models.CharField(
        max_length=255, help_text="Subtitle for the video section"
    )
    description = models.TextField(help_text="Description of the video section")
    search_placeholder = models.CharField(
        max_length=255, default="Search videos...", help_text="Search placeholder text"
    )
    no_results = models.CharField(
        max_length=255, default="No videos found", help_text="No results message"
    )
    try_adjusting = models.CharField(
        max_length=255,
        default="Try adjusting your search or filters",
        help_text="Try adjusting message",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Video Section"
        verbose_name_plural = "Video Sections"
        indexes = [
            models.Index(fields=["is_active", "is_deleted"], name="video_section_active"),
        ]

    def __str__(self):
        return self.title
