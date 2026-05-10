from django.contrib import admin

from home.models import HeroSection


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "subtitle",
        "button_text",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["title", "subtitle", "description"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Content", {"fields": ("title", "subtitle", "description")}),
        ("Button Configuration", {"fields": ("button_text", "button_link")}),
        (
            "Background Settings",
            {
                "fields": (
                    "background_gradient",
                    "background_image_url",
                    "background_image",
                )
            },
        ),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
