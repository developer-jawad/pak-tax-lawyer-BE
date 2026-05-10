from common.api.serializers import DynamicFieldsModelSerializer

from service.models import ServiceStatistic


class ServiceStatisticSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ServiceStatistic
        fields = [
            'id',
            'number',
            'label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
