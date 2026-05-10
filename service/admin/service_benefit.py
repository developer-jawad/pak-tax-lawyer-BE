from django.contrib import admin

from service.models import ServiceBenefit


@admin.register(ServiceBenefit)
class ServiceBenefitAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon', 'text', 'created_at', 'updated_at']
    search_fields = ['icon', 'text']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Benefit Content', {
            'fields': ('icon', 'text')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
