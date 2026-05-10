from django.contrib import admin

from about.models import AboutStatistic


@admin.register(AboutStatistic)
class AboutStatisticAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "number",
        "label",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["number", "label"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Statistic Content", {"fields": ("number", "label")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
