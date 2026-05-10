from django.contrib import admin

from home.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'role',
        'company',
        'rating',
        'location',
        'featured',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_filter = ['featured', 'rating', 'is_active', 'is_deleted', 'created_at']
    search_fields = ['name', 'role', 'company', 'testimonial', 'location']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'role', 'company', 'avatar')
        }),
        ('Testimonial Content', {
            'fields': ('rating', 'testimonial', 'location')
        }),
        ('Featured Settings', {
            'fields': ('featured',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
