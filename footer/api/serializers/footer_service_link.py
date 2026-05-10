from common.api.serializers import DynamicFieldsModelSerializer

from footer.models import FooterServiceLink


class FooterServiceLinkSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterServiceLink
        fields = [
            'id',
            'label',
            'url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
