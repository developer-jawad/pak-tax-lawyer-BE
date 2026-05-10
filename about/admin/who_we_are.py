from django.contrib import admin

from about.models import WhoWeAre


@admin.register(WhoWeAre)
class WhoWeAreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'subtitle',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['title', 'subtitle']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Who We Are Content', {
            'fields': ('subtitle', 'title', 'paragraphs', 'image_overlay_title', 'image_overlay_description')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
