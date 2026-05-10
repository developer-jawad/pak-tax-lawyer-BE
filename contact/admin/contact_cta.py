from django.contrib import admin

from contact.models import ContactCTA


@admin.register(ContactCTA)
class ContactCTAAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "icon",
        "title",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["icon", "title"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("CTA Content", {"fields": ("icon", "title", "description")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
