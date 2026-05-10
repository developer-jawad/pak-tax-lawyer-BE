from about.models import AboutValue
from common.api.serializers import DynamicFieldsModelSerializer


class AboutValueSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutValue
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
