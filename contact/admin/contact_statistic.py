from django.contrib import admin

from contact.models import ContactStatistic


@admin.register(ContactStatistic)
class ContactStatisticAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "icon",
        "value",
        "label",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["icon", "value", "label"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Statistic Content", {"fields": ("icon", "value", "label")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
