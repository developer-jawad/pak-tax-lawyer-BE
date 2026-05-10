from django.contrib import admin

from footer.models import FooterLegalLink


@admin.register(FooterLegalLink)
class FooterLegalLinkAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "label",
        "url",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["label", "url"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Legal Link Content", {"fields": ("label", "url")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
