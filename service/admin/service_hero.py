from django.contrib import admin

from service.models import ServiceHero


@admin.register(ServiceHero)
class ServiceHeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title', 'subtitle']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Hero Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
