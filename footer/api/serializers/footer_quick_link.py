from common.api.serializers import DynamicFieldsModelSerializer

from footer.models import FooterQuickLink


class FooterQuickLinkSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterQuickLink
        fields = [
            'id',
            'label',
            'url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
