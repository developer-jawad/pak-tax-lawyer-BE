from common.api.serializers import DynamicFieldsModelSerializer

from footer.models import FooterContact


class FooterContactSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterContact
        fields = [
            'id',
            'title',
            'address_label',
            'address_value',
            'phone_label',
            'phone_value',
            'email_label',
            'email_value',
            'business_hours_label',
            'business_hours_value',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
