from django.contrib import admin

from service.models import ServiceCTA


@admin.register(ServiceCTA)
class ServiceCTAAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'is_deleted', 'is_service_section', 'title', 'button_text', 'button_link', 'created_at', 'updated_at']
    list_filter = ['is_active', 'is_deleted', 'is_service_section']
    search_fields = ['title', 'description', 'button_text', 'button_link']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('CTA Configuration', {
            'fields': ('is_service_section',)
        }),
        ('CTA Content', {
            'fields': ('title', 'description', 'button_text', 'button_link')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
