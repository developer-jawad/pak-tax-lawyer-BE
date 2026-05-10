from django.contrib import admin

from videos.models import VideoSection


@admin.register(VideoSection)
class VideoSectionAdmin(admin.ModelAdmin):
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
        ('Section Content', {
            'fields': ('title', 'subtitle', 'description', 'search_placeholder', 'no_results', 'try_adjusting')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
