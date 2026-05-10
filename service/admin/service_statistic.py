from django.contrib import admin

from service.models import ServiceStatistic


@admin.register(ServiceStatistic)
class ServiceStatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'label', 'created_at', 'updated_at']
    search_fields = ['number', 'label']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Statistic Content', {
            'fields': ('number', 'label')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
