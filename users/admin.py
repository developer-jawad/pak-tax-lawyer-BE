from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


class UserInline(admin.TabularInline):
    model = User
    fields = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
    )
    readonly_fields = ("email", "first_name", "last_name", "is_staff", "date_joined")
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("email", "password", "is_active", "is_staff", "is_superuser")},
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
