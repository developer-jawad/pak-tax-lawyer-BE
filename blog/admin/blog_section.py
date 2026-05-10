from django.contrib import admin

from blog.models import BlogSection


@admin.register(BlogSection)
class BlogSectionAdmin(admin.ModelAdmin):
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
            'fields': ('subtitle', 'title', 'description', 'categories')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
