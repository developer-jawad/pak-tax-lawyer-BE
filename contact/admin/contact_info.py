from django.contrib import admin

from contact.models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "icon",
        "title",
        "details",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["icon", "title", "details"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Contact Info Content", {"fields": ("icon", "title", "details", "subtitle")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
