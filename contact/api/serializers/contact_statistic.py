from common.api.serializers import DynamicFieldsModelSerializer

from contact.models import ContactStatistic


class ContactStatisticSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ContactStatistic
        fields = [
            'id',
            'icon',
            'value',
            'label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
