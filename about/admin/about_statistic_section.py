from django.contrib import admin

from about.models import AboutStatisticSection


@admin.register(AboutStatisticSection)
class AboutStatisticSectionAdmin(admin.ModelAdmin):
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
        ("Statistic Section Content", {"fields": ("title",)}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
