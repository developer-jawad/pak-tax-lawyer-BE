from django.contrib import admin

from service.models import ServiceHero


@admin.register(ServiceHero)
class ServiceHeroAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "is_active",
        "is_deleted",
        "title",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title", "subtitle"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Hero Content", {"fields": ("title", "subtitle")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
