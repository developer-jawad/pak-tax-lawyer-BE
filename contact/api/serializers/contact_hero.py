from common.api.serializers import DynamicFieldsModelSerializer
from contact.models import ContactHero


class ContactHeroSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactHero
        fields = [
            "id",
            "title",
            "subtitle",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
