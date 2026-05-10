from common.api.serializers import DynamicFieldsModelSerializer
from home.models import TestimonialSection


class TestimonialSectionSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TestimonialSection
        fields = [
            "id",
            "subtitle",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
