from django.contrib import admin

from home.models import TestimonialCTA


@admin.register(TestimonialCTA)
class TestimonialCTAAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'is_active',
        'is_deleted',
        'title',
        'button_text',
        'is_testimonial_section',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'is_testimonial_section', 'created_at']
    search_fields = ['title', 'description', 'button_text']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('CTA Content', {
            'fields': ('title', 'description', 'button_text', 'button_link')
        }),
        ('Settings', {
            'fields': ('is_testimonial_section',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
