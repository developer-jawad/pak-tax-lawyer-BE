from common.api.serializers import DynamicFieldsModelSerializer

from about.models import AboutStatistic


class AboutStatisticSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AboutStatistic
        fields = [
            'id',
            'number',
            'label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
