from django.contrib import admin

from blog.models import BlogPost, Tag, ContentBlock


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "is_active", "created_at"]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["created_at", "updated_at"]


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content_type",
        "content_preview",
        "order",
        "is_active",
        "created_at",
    ]
    list_filter = ["content_type", "is_active", "is_deleted", "created_at"]
    search_fields = ["content"]
    readonly_fields = ["created_at", "updated_at"]

    def content_preview(self, obj):
        if isinstance(obj.content, str):
            return obj.content[:100] + "..." if len(obj.content) > 100 else obj.content
        elif isinstance(obj.content, list):
            preview = str(obj.content)[:100]
            return preview + "..." if len(preview) > 100 else preview
        return str(obj.content)[:100]
    content_preview.short_description = "Content"


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "author_name",
        "category",
        "date",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["category", "is_active", "is_deleted", "date", "created_at"]
    search_fields = ["title", "excerpt", "author_name"]
    readonly_fields = ["created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags", "content_blocks", "related_posts"]

    fieldsets = (
        (
            "Blog Content",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "author_name",
                    "author_title",
                    "author_avatar",
                    "author_bio",
                    "category",
                )
            },
        ),
        ("Publication Details", {"fields": ("date", "read_time")}),
        ("Tags", {"fields": ("tags",)}),
        ("Image", {"fields": ("image_url", "image")}),
        ("Content Blocks", {"fields": ("content_blocks",)}),
        ("Related Posts", {"fields": ("related_posts",)}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
