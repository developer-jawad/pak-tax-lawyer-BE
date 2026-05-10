from common.api.serializers import DynamicFieldsModelSerializer
from contact.models import ContactCTA


class ContactCTASerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactCTA
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
