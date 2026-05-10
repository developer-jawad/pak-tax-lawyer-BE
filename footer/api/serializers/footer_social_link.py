from common.api.serializers import DynamicFieldsModelSerializer

from footer.models import FooterSocialLink


class FooterSocialLinkSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterSocialLink
        fields = [
            'id',
            'platform',
            'url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
