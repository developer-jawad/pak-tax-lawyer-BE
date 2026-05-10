from django.contrib import admin

from service.models import ServiceCTA


@admin.register(ServiceCTA)
class ServiceCTAAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'button_text', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'button_text']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('CTA Content', {
            'fields': ('title', 'description', 'button_text')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
