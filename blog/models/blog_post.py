from django.db import models

from common.constants import BLOG_CATEGORIES, BLOG_CATEGORY_CHOICES
from common.managers import ActiveObjectsManager
from common.models import BaseModel


class BlogPost(BaseModel):
    title = models.CharField(max_length=255, help_text="Blog post title")
    excerpt = models.TextField(help_text="Short excerpt of the blog post")
    author = models.CharField(max_length=255, help_text="Author name")
    date = models.DateField(help_text="Publication date")
    read_time = models.CharField(
        max_length=50, help_text="Read time (e.g., '5 min read')"
    )
    category = models.IntegerField(
        choices=BLOG_CATEGORY_CHOICES,
        default=BLOG_CATEGORIES.all,
        help_text="Blog category",
    )
    image_url = models.URLField(
        max_length=1000, blank=True, null=True, help_text="External URL for blog image"
    )
    image = models.ImageField(
        upload_to="blog_posts/", blank=True, null=True, help_text="Upload blog image"
    )
    slug = models.SlugField(
        unique=True, max_length=255, help_text="URL slug for the blog post"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
