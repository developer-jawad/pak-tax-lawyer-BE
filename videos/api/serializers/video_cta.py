from common.api.serializers import DynamicFieldsModelSerializer
from videos.models import VideoCTA


class VideoCTASerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = VideoCTA
        fields = [
            "id",
            "title",
            "description",
            "video_count",
            "video_count_label",
            "button_text",
            "button_link",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
