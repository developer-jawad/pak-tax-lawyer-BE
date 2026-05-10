from common.api.serializers import DynamicFieldsModelSerializer
from contact.models import ContactInfo


class ContactInfoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            "id",
            "icon",
            "title",
            "details",
            "subtitle",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
