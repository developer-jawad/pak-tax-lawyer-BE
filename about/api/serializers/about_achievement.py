from about.models import AboutAchievement
from common.api.serializers import DynamicFieldsModelSerializer


class AboutAchievementSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutAchievement
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
