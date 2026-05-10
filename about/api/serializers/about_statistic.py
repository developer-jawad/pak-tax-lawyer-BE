from about.models import AboutStatistic
from common.api.serializers import DynamicFieldsModelSerializer


class AboutStatisticSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutStatistic
        fields = [
            "id",
            "number",
            "label",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
