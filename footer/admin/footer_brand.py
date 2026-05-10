from django.contrib import admin

from footer.models import FooterBrand


@admin.register(FooterBrand)
class FooterBrandAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'logo_alt',
        'follow_us',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['name', 'logo_alt', 'follow_us']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Brand Content', {
            'fields': ('name', 'description', 'logo_alt', 'follow_us')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
