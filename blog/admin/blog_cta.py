from django.contrib import admin

from blog.models import BlogCTA


@admin.register(BlogCTA)
class BlogCTAAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "is_active",
        "is_deleted",
        "button_text",
        "button_link",
        "is_blog_section",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "is_blog_section", "created_at"]
    search_fields = ["button_text", "button_link"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("CTA Content", {"fields": ("button_text", "button_link")}),
        ("Settings", {"fields": ("is_blog_section",)}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
