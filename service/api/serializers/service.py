from rest_framework import serializers

from common.api.serializers import DynamicFieldsModelSerializer
from service.models import Service


class ServiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "description",
            "icon",
            "color",
            "button_text",
            "badge",
            "popular",
            "features",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
