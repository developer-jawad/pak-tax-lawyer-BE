from common.api.serializers import DynamicFieldsModelSerializer

from contact.models import ContactMap


class ContactMapSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactMap
        fields = [
            'id',
            'title',
            'iframe_url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
