from django.contrib import admin

from contact.models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active',
        'is_deleted',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_active', 'is_deleted', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Form Content', {
            'fields': ('title', 'description', 'name_label', 'email_label', 'phone_label', 'subject_label', 'message_label', 'submit_button_text', 'loading_text', 'success_message')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
