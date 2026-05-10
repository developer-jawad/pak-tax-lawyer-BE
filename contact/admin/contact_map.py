from django.contrib import admin

from contact.models import ContactMap


@admin.register(ContactMap)
class ContactMapAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["title"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Map Content", {"fields": ("title", "iframe_url")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
