from common.api.serializers import DynamicFieldsModelSerializer
from footer.models import FooterLegalLink


class FooterLegalLinkSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterLegalLink
        fields = [
            "id",
            "label",
            "url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
