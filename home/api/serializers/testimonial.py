from rest_framework import serializers

from common.api.serializers import DynamicFieldsModelSerializer
from home.models import Testimonial


class TestimonialSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Testimonial
        fields = [
            "id",
            "name",
            "role",
            "company",
            "avatar",
            "rating",
            "testimonial",
            "location",
            "featured",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
