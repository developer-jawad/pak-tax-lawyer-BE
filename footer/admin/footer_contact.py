from django.contrib import admin

from footer.models import FooterContact


@admin.register(FooterContact)
class FooterContactAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "phone_value",
        "email_value",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted", "created_at"]
    search_fields = ["title", "address_value", "phone_value", "email_value"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (
            "Contact Content",
            {
                "fields": (
                    "title",
                    "address_label",
                    "address_value",
                    "phone_label",
                    "phone_value",
                    "email_label",
                    "email_value",
                    "business_hours_label",
                    "business_hours_value",
                )
            },
        ),
        ("Status", {"fields": ("is_active", "is_deleted")}),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
