from django.contrib import admin

from footer.models import FooterSocialLink


@admin.register(FooterSocialLink)
class FooterSocialLinkAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "platform",
        "url",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at", "platform"]
    search_fields = ["platform", "url"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Social Link Content", {"fields": ("platform", "url")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
