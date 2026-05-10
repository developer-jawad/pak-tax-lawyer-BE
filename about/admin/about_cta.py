from django.contrib import admin

from about.models import AboutCTA


@admin.register(AboutCTA)
class AboutCTAAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'phone',
        'email',
        'button_text',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['title', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('CTA Content', {
            'fields': ('title', 'description', 'phone', 'email', 'button_text', 'button_link')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
