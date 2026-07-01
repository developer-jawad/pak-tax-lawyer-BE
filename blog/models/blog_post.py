from django.db import models

from common.constants import BLOG_CATEGORIES, BLOG_CATEGORY_CHOICES
from common.managers import ActiveObjectsManager
from common.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True, help_text="Tag name")
    slug = models.SlugField(max_length=100, unique=True, help_text="URL slug for tag")

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ContentBlock(BaseModel):
    CONTENT_TYPE_CHOICES = [
        ("heading", "Heading"),
        ("paragraph", "Paragraph"),
        ("list", "List"),
        ("ordered-list", "Ordered List"),
        ("quote", "Quote"),
        ("highlight", "Highlight"),
        ("subheading", "Subheading"),
    ]

    content_type = models.CharField(
        max_length=50,
        choices=CONTENT_TYPE_CHOICES,
        help_text="Type of content block",
    )
    content = models.JSONField(help_text="Content data for the block")
    order = models.PositiveIntegerField(
        default=0, help_text="Order of the content block"
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"
        ordering = ["order"]

    def __str__(self):
        content_preview = (
            str(self.content)[:50] + "..."
            if len(str(self.content)) > 50
            else str(self.content)
        )
        return f"{self.get_content_type_display()} (Order: {self.order}) - {content_preview}"


class BlogPost(BaseModel):
    title = models.CharField(max_length=255, help_text="Blog post title")
    excerpt = models.TextField(help_text="Short excerpt of the blog post")
    author_name = models.CharField(max_length=255, help_text="Author name")
    author_title = models.CharField(
        max_length=255, blank=True, null=True, help_text="Author title/position"
    )
    author_avatar = models.URLField(
        max_length=1000, blank=True, null=True, help_text="Author avatar URL"
    )
    author_bio = models.TextField(blank=True, null=True, help_text="Author bio")
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
    tags = models.ManyToManyField(
        "Tag",
        blank=True,
        related_name="blog_posts",
        help_text="Tags associated with the blog post",
    )
    content_blocks = models.ManyToManyField(
        "ContentBlock",
        blank=True,
        related_name="blog_posts",
        help_text="Content blocks for the blog post",
    )
    related_posts = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="related_to",
        help_text="Related blog posts",
    )

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-date", "-created_at"]
        indexes = [
            models.Index(fields=["slug"], name="blog_post_slug_idx"),
            models.Index(fields=["is_active", "is_deleted", "-date"], name="blog_post_active_date_idx"),
            models.Index(fields=["category", "is_active", "is_deleted"], name="blog_post_category_idx"),
        ]

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url
