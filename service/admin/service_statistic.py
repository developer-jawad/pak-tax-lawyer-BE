from django.contrib import admin

from service.models import ServiceStatistic


@admin.register(ServiceStatistic)
class ServiceStatisticAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "is_active",
        "is_deleted",
        "number",
        "label",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
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
