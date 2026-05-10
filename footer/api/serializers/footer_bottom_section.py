from common.api.serializers import DynamicFieldsModelSerializer
from footer.models import FooterBottomSection


class FooterBottomSectionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterBottomSection
        fields = [
            "id",
            "copyright",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
