from about.models import WhoWeAre
from common.api.serializers import DynamicFieldsModelSerializer


class WhoWeAreSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = WhoWeAre
        fields = [
            "id",
            "subtitle",
            "title",
            "paragraphs",
            "image_overlay_title",
            "image_overlay_description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
