from common.api.serializers import DynamicFieldsModelSerializer
from footer.models import FooterBrand


class FooterBrandSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = FooterBrand
        fields = [
            "id",
            "name",
            "description",
            "logo_alt",
            "follow_us",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
