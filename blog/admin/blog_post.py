from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "author",
        "category",
        "date",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["category", "is_active", "is_deleted", "date", "created_at"]
    search_fields = ["title", "excerpt", "author"]
    readonly_fields = ["created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        (
            "Blog Content",
            {"fields": ("title", "slug", "excerpt", "author", "category")},
        ),
        ("Publication Details", {"fields": ("date", "read_time")}),
        ("Image", {"fields": ("image_url", "image")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
