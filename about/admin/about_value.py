from django.contrib import admin

from about.models import AboutValue


@admin.register(AboutValue)
class AboutValueAdmin(admin.ModelAdmin):
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
    search_fields = ["title"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Value Content", {"fields": ("icon", "title", "description")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
