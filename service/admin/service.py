from django.contrib import admin

from service.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'icon',
        'badge',
        'popular',
        'created_at',
        'updated_at',
    ]
    list_filter = ['badge', 'popular', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Service Content', {
            'fields': ('title', 'description', 'icon', 'color', 'button_text', 'badge', 'popular')
        }),
        ('Features', {
            'fields': ('features',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
