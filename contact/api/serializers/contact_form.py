from common.api.serializers import DynamicFieldsModelSerializer

from contact.models import ContactForm


class ContactFormSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactForm
        fields = [
            'id',
            'title',
            'description',
            'name_label',
            'email_label',
            'phone_label',
            'subject_label',
            'message_label',
            'submit_button_text',
            'loading_text',
            'success_message',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
