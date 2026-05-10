from about.models import AboutCTA
from common.api.serializers import DynamicFieldsModelSerializer


class AboutCTASerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutCTA
        fields = [
            "id",
            "title",
            "description",
            "phone",
            "email",
            "button_text",
            "button_link",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
