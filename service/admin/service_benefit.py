from django.contrib import admin

from service.models import ServiceBenefit


@admin.register(ServiceBenefit)
class ServiceBenefitAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "is_active",
        "is_deleted",
        "icon",
        "text",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["icon", "text"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Benefit Content", {"fields": ("icon", "text")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
