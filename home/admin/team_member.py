from django.contrib import admin

from home.models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'position',
        'specialization',
        'featured',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_filter = ['featured', 'is_active', 'is_deleted', 'created_at']
    search_fields = ['name', 'position', 'specialization', 'bio']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'specialization', 'avatar')
        }),
        ('Biography', {
            'fields': ('bio', 'credentials')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'linkedin')
        }),
        ('Featured Settings', {
            'fields': ('featured', 'featured_label')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
