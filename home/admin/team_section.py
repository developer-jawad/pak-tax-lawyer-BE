from django.contrib import admin

from home.models import TeamSection


@admin.register(TeamSection)
class TeamSectionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'is_active',
        'is_deleted',
        'title',
        'subtitle',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at', 'updated_at']
    search_fields = ['title', 'subtitle', 'description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Section Content', {
            'fields': ('subtitle', 'title', 'description', 'credentials_label')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
