from common.api.serializers import DynamicFieldsModelSerializer

from about.models import AboutStatisticItem


class AboutStatisticItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutStatisticItem
        fields = [
            'id',
            'icon',
            'value',
            'label',
            'color',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
