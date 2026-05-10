from common.api.serializers import DynamicFieldsModelSerializer
from service.models import ServiceHero


class ServiceHeroSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ServiceHero
        fields = [
            "id",
            "title",
            "subtitle",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
