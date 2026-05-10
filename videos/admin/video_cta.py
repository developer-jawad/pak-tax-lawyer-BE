from django.contrib import admin

from videos.models import VideoCTA


@admin.register(VideoCTA)
class VideoCTAAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'video_count',
        'button_text',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('CTA Content', {
            'fields': ('title', 'description', 'video_count', 'video_count_label', 'button_text', 'button_link')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
