from django.contrib import admin

from service.models import (
    Service,
    ServiceSection,
)


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    fields = ['title', 'icon', 'color', 'button_text', 'badge', 'popular']


@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'subtitle',
        'cta_title',
        'created_at',
        'updated_at',
    ]
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'subtitle', 'description', 'cta_title']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [
        ServiceInline,
    ]
    
    fieldsets = (
        ('Section Content', {
            'fields': ('subtitle', 'title', 'description')
        }),
        ('CTA Configuration', {
            'fields': ('cta_title', 'cta_description', 'primary_button', 'secondary_button')
        }),
        ('Features Label', {
            'fields': ('features_label',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
