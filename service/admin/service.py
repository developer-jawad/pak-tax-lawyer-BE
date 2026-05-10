from django.contrib import admin

from service.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'is_active',
        'is_deleted',
        'title',
        'icon',
        'badge',
        'popular',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'badge', 'popular', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Service Content', {
            'fields': ('title', 'description', 'icon', 'color', 'button_text', 'badge', 'popular')
        }),
        ('Features', {
            'fields': ('features',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
