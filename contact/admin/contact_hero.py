from django.contrib import admin

from contact.models import ContactHero


@admin.register(ContactHero)
class ContactHeroAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "subtitle",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["title", "subtitle"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        ("Hero Content", {"fields": ("title", "subtitle", "description")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
