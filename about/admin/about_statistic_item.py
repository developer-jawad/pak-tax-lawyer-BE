from django.contrib import admin

from about.models import AboutStatisticItem


@admin.register(AboutStatisticItem)
class AboutStatisticItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'icon',
        'value',
        'label',
        'color',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['value', 'label']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Statistic Item Content', {
            'fields': ('icon', 'value', 'label', 'color')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
