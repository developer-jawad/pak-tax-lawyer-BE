from common.api.serializers import DynamicFieldsModelSerializer
from service.models import ServiceCTA


class ServiceCTASerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ServiceCTA
        fields = [
            "id",
            "title",
            "description",
            "button_text",
            "button_link",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
