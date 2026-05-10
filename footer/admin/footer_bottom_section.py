from django.contrib import admin

from footer.models import FooterBottomSection


@admin.register(FooterBottomSection)
class FooterBottomSectionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'copyright',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['copyright']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Bottom Section Content', {
            'fields': ('copyright',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
