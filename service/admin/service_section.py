from django.contrib import admin

from service.models import Service, ServiceSection


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    fields = ["title", "icon", "color", "button_text", "badge", "popular"]


@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "is_active",
        "is_deleted",
        "title",
        "subtitle",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at", "updated_at"]
    search_fields = ["title", "subtitle", "description"]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [
        ServiceInline,
    ]

    fieldsets = (
        ("Section Content", {"fields": ("subtitle", "title", "description")}),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
