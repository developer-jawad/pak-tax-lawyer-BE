from django.contrib import admin

from home.models import TeamCTA


@admin.register(TeamCTA)
class TeamCTAAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'is_active',
        'is_deleted',
        'title',
        'email',
        'is_team_section',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'is_team_section', 'created_at']
    search_fields = ['title', 'description', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('CTA Content', {
            'fields': ('title', 'description', 'email')
        }),
        ('Settings', {
            'fields': ('is_team_section',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
