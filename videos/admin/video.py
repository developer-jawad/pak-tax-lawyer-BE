from django.contrib import admin

from videos.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "category",
        "duration",
        "views",
        "trending",
        "new",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "category",
        "trending",
        "new",
        "is_active",
        "is_deleted",
        "created_at",
    ]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (
            "Video Content",
            {
                "fields": (
                    "title",
                    "description",
                    "thumbnail",
                    "duration",
                    "views",
                    "category",
                    "video_url",
                )
            },
        ),
        ("Flags", {"fields": ("trending", "new")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
